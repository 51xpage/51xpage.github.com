---
layout: post
title: "道听途说nginx系列3 - 反向代理"
description: "nginx反向代理"
category: "nginx"
tags: "nginx 网络 反向代理 proxy"
---
{% include JB/setup %}

## 场景描述
企业对外提供

## 反向代理
   反向代理是相对于我平常所说的代理而言的。
   在企业内部，通过一台专门的服务器连接外部网络，即互联网，这台服务器就是**代理服务器**。它汇聚所有设备的上网请求进行转发，不需要每台设备都配置专用的拨号账号，节约资源。  
   
	（企业内部用户） --> 代理服务器  --> (外部网站)
   
   企业内部有很多系统，如果都对外开放，需要很多连接入口，而通过统一的代理服务器，可以只对外开放这一台服务器，由它把把外部用户的请求，转发到具体的应用系统。从数据的流向来看，它和用户代理上网正好相反，所以反向代理。
   
	(外部用户) --> 代理服务器 --> (内部应用系统)

## 业务场景

四、Nginx之反向代理
五、Nginx之负载均衡
六、Nginx之页面缓存
七、Nginx之URL重写
八、Nginx之读写分离	
	
## 配置样例
  就配置而言，nginx提供了很简单的方式，提供一个关键字 `upstream`
  {% highlight json %} 
  upstream  cluster01
  # 定义一个cluster01的集群
  {
  	server 192.168.1.12:80 weight = 3;
  	server 192.168.1.13:80 weight = 3;
  	server 192.168.1.14:80 weight = 3;
  	# 这个集群里面有3个服务器，
  }
  
  server {
  	listen  80;
  	server_name test;
  	location /{
  		proxy_pass http://cluster01
  		# 请求会分发到集群去
  	}
  }
  {% endhighlight  %}
 
## 参数详解

#### 如果某个服务器配置较好，优先处理如何配置？
  可以通过weight来设置权重，默认是1，数字大的优先级高
  
#### 如果某个服务器一直连不上，如何废弃？
  可以通过max_fails和fail_timeout配置，如 
  {% highlight json %}  
  server 192.168.1.13:80  max_fails=3 fail_timeout=30s;
  {% endhighlight  %} 
  
  * max_fails表示nginx和这个服务器尝试失败的次数和超时时间
  * 如果超过次数，这个服务器就从集群中剔除，下次不再分发
  * 如果为0，就表示一直认为服务器可用  
 
#### 如果某个服务器平时闲置，当主服务器不行了才启用？
  可以增加backup关键字，如  
  {% highlight json %} 
  server 192.168.0.2  backup
  {% endhighlight  %} 
  
#### 如何保障用户请求一直在某台服务器上？
  可以增加ip_hash参数，nginx会把ip地址hash，形成一个唯一的散列值，用来和后台服务器匹配。  
{% highlight json %}   
upstream cluster01 {
   ip_hash;

   server 192.168.1.12:80 weight = 3;
   server 192.168.1.13:80 weight = 3;
   server 192.168.1.14:80 weight = 3;
}   
{% endhighlight  %} 

#### 如果临时移除某个服务器，但是老的客户端请求继续
  接ip_hash问题，如果已经有客户端连到某个服务器了，但是需要临时移除，这个时候可以加一个参数down，表示这个服务器不再接受新的请求，但是老的请求继续处理。
{% highlight json %}  
upstream cluster01 {
   ip_hash;

   server 192.168.1.12:80 weight = 3;
   server 192.168.1.13:80 weight = 3 down;
   server 192.168.1.14:80 weight = 3;
}  
{% endhighlight  %}   

	ip_hash只是一种负载均衡方法，还有几种其他的方法，有机会再更新
	
#### 如何把真实地址带给目标服务器
	
有了上面的配置，我们知道如何将请求转发给真实的地址。但是有个问题，目标系统如果通过CGI变量remote_addr，获取的是nginx这个服务器的地址。而不是用户的真实地址，解决办法也很简单。通过**proxy_set_header**把请求头带到目标服务器
	
{% highlight json %} 
  
  	location /{
  		proxy_pass http://cluster01
  		proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
  	}
  }
  {% endhighlight  %}
 
 在python里面，后台拿到的时候，这个变量会变成全大写的一个变量**HTTP_X_REAL_IP**。
	如果想要设置这个地址，在Flask，可以在请求处理前设置。
{% highlight json %} 	
	
@app.before_request  
def pre_request_logging():  
    # 解决nginx的地址问题，要不然处理短信登录限制就不行了  
    if 'HTTP_X_REAL_IP' in request.environ:  
        request.environ['REMOTE_ADDR'] = request.environ['HTTP_X_REAL_IP']  
 {% endhighlight  %}

* X-Real_Ip  
   用户真实ip地址
* X-Forwarded-For  
  用于记录代理信息的，每经过一个代理，就累加一次
	
	