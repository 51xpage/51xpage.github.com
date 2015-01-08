---
layout: post
title: "道听途说nginx系列1 - 安装"
description: "nginx起步"
category: "nginx"
tags: "nginx 网络 反向代理 proxy"
---
{% include JB/setup %}

##准备工作
为nginx运行的专门的指定用户下  

*  建群组  
{% highlight shell %}  
  groupadd -r nginx  
{% endhighlight  %}
*	建用户  
{% highlight shell %}   
  useradd -r -g nginx -M nginx  
{% endhighlight  %}

##源码安装
* 下载源码  
  可以从nginx的官方网站[http://nginx.org/](http://nginx.org/ "http://nginx.org/")下载最新版  
  如果服务器可以上网，也可以直接通过命令下载，如  
  `wget http://nginx.org/download/nginx-1.6.2.tar.gz`
  
		nginx官网提供了3种版本下载：
		Mainline ：开发版
		Stable：最新稳定版，生产环境上建议使用的版本
		Legacy：以前的稳定版

* 解压  
{% highlight shell %}  
  tar  zxvf  nginx-1.6.2.tar.gz  -C /local/nginx/  
  cd cd  /local/nginx/nginx-1.6.2
{% endhighlight  %}  
* 编译  
	* configure  
		进入目录以后会发现有一个configure文件，个人的理解，confirgure就2个目的
		* 检查当前的编译条件是否具备。如依赖库是否存在等
		* 生成MakeFile文件，用于后面的make。也因此所以会带一些参数，下面是示例，这些参数可以不带
	
		比如好启用ssl，就要带ssl模块，如果要监控nginx，就启用stub，如果要启用smtp等邮件服务，就带上mail模块
{% highlight shell %}  
  ./configure \  
  --prefix=/usr/local/nginx \   # 设置路径前缀  
  --user=nginx \  
  --group=nginx \  
  --with-http_ssl_module \  
  --with-http_stub_status_module \ 
  --with-pcre  
{% endhighlight  %}  

	* 编译安装  
{% highlight shell %}  
	`make && make install`	
{% endhighlight  %}  

* 启动  

* 测试运行


{% highlight java %}
public class HelloWorld {
    public static void main(String args[]) {
      System.out.println("Hello World!");
    }
}
{% endhighlight %}

* 配置服务  
	为了方便使用，可以为nginx创建一个服务脚本。  
    `vi /etc/init.d/nginx`  
    内容如下：  
	    `#!/bin/bash`  
	 	`#description: Nginx Service Control Script`  
	 	`case "$1" in`  
		  ` start)`  
		  	`  /usr/local/nginx/nginx`  
		  `;;`  
	     ` stop)`  
	  `        /usr/bin/killall -s QUIT nginx`  
	      `       ;;`  
	  ` restart)`  
	        `  $0 stop`  
	     `     $0 start`  
	 `         ;;`  
	       reload)  
	         ` /usr/bin/killall -s HUP nginx`  
	        `  ;;`  
	 `  *)`  
	     `echo "Usage:$0 {start|stop|restart|reload}"`  
	    ` exit 1`  
	    ` esac`  
	     `exit 0  `

* 自启动
  

##rpm安装
  目前从网络上能找到的大部分是源码方式安装。实际上正式环境并不推荐采用源码安装的方式，个人理解是因为通常不具备编译环境和相关包，可能还会有潜在的影响？
