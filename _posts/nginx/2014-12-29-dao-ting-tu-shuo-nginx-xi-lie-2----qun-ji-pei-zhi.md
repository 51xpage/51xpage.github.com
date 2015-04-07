---
layout: post
title: "道听途说nginx系列2 - 群集配置"
description: "nginx负载均衡"
category: "nginx"
tags: "nginx 网络 cluster"
---
{% include JB/setup %}

   现在我们已经可以运行nginx，并让nginx来提供一些能力。  


## 负载均衡
   通常而言，对于大型系统而言，大并发，大用户量请求，由1台服务器来处理是不现实的，单台服务器的硬件资源有限，很容易就会出现瓶颈。这个时候我们就希望能通过不同的服务器，提供相同的功能，来分担压力，均衡负载。
   负载均衡更多的是分担计算能力。

## 失效转移
   现实情况下，对于分布式系统而言，服务器异常是很正常的事情。和负载均衡类似。所以我们需要在服务器失效的时候，能够快速恢复对外服务。负载均衡意味着相同功能的服务器一直处于活动状态。而失效转移更多的是指几台功能相同的服务器，当一台出现故障时，能快速切换到另外一台服务器。而这台服务器可能只是处于等待状态，原来并不提供功能。
   
总而言之，为了区分功能相同的服务器，就有了cluster的概念，即群集。群集中的服务器功能一致，统一管理。  

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