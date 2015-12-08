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
{% highlight bash %}  
  groupadd -r nginx  
{% endhighlight  %}
*	建用户  
{% highlight bash %}   
  useradd -r -g nginx -M nginx  
{% endhighlight  %}

##源码安装
* 下载源码  
  可以从nginx的官方网站[http://nginx.org/](http://nginx.org/ "http://nginx.org/")下载最新版  
  如果服务器可以上网，也可以直接通过命令下载，如  
{% highlight bash %}
  wget http://nginx.org/download/nginx-1.6.2.tar.gz
{% endhighlight  %}  
  
	nginx官网提供了3种版本下载：
	* Mainline ：开发版  
	* Stable：最新稳定版，生产环境上建议使用的版本  
	* Legacy：以前的稳定版  

* 解压  
{% highlight bash %}  
	tar  zxvf  nginx-1.6.2.tar.gz  -C /local/nginx/  
	cd   /local/nginx/nginx-1.6.2
{% endhighlight  %}  
* 编译  
	* configure  
		进入目录以后会发现有一个configure文件，个人的理解，confirgure就2个目的
		* 检查当前的编译条件是否具备。如依赖库是否存在等
		* 生成MakeFile文件，用于后面的make。也因此所以会带一些参数，下面是示例，这些参数可以不带
	
		比如好启用ssl，就要带ssl模块，如果要监控nginx，就启用stub，如果要启用smtp等邮件服务，就带上mail模块
{% highlight bash %}  
  ./configure \  
  --prefix=/usr/local/nginx \   # 设置路径前缀  
  --user=nginx \  
  --group=nginx \  
  --with-http_ssl_module \  
  --with-http_stub_status_module \ 
  --with-pcre  
{% endhighlight  %}  

	* 编译安装  
{% highlight bash %}  
	make && make install	
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
~~~ bash 
    vi /etc/init.d/nginx  
~~~
    内容如下：  
{% highlight bash %}
	#!/bin/bash  
	#description: Nginx Service Control Script  
	case "$1" in  
	   start)  
	  	/usr/local/nginx/nginx  
		;;  
	   stop)  
	        /usr/bin/killall -s QUIT nginx  
	        ;;  
	   restart)  
	        $0 stop  
	        $0 start  
	        ;;  
	   reload)  
	        /usr/bin/killall -s HUP nginx  
	        ;;  
	 *)  
	 echo "Usage:$0 {start|stop|restart|reload}"  
	 exit 1  
	 esac  
	 exit 0  
{% endhighlight  %}  

* 自启动
  

##rpm安装
  目前从网络上能找到的大部分是源码方式安装。实际上正式环境并不推荐采用源码安装的方式，个人理解是因为通常不具备编译环境和相关包，可能还会有潜在的影响？
  
  {% highlight bash %}
  rpm -ivh xxx.rpm
  {% endhighlight %}
  
## 一次失败安装

在CentOS 7上安装了几台nginx，有一次安装失败了。提示信息如下
{% highlight bash %}

[root@libunwind-1.1]# yum install nginx
Loaded plugins: langpacks
Resolving Dependencies
--> Running transaction check
---> Package nginx.x86_64 1:1.6.3-7.el7 will be installed
--> Processing Dependency: nginx-filesystem = 1:1.6.3-7.el7 for package: 1:nginx-1.6.3-7.el7.x86_64
--> Processing Dependency: nginx-filesystem for package: 1:nginx-1.6.3-7.el7.x86_64
--> Processing Dependency: libxslt.so.1(LIBXML2_1.0.18)(64bit) for package: 1:nginx-1.6.3-7.el7.x86_64
--> Processing Dependency: libxslt.so.1(LIBXML2_1.0.11)(64bit) for package: 1:nginx-1.6.3-7.el7.x86_64
--> Processing Dependency: gd for package: 1:nginx-1.6.3-7.el7.x86_64
--> Processing Dependency: GeoIP for package: 1:nginx-1.6.3-7.el7.x86_64
--> Processing Dependency: libxslt.so.1()(64bit) for package: 1:nginx-1.6.3-7.el7.x86_64
--> Processing Dependency: libprofiler.so.0()(64bit) for package: 1:nginx-1.6.3-7.el7.x86_64
--> Processing Dependency: libgd.so.2()(64bit) for package: 1:nginx-1.6.3-7.el7.x86_64
--> Processing Dependency: libexslt.so.0()(64bit) for package: 1:nginx-1.6.3-7.el7.x86_64
--> Processing Dependency: libGeoIP.so.1()(64bit) for package: 1:nginx-1.6.3-7.el7.x86_64
--> Running transaction check
---> Package GeoIP.x86_64 0:1.5.0-9.el7 will be installed
---> Package gd.x86_64 0:2.0.35-26.el7 will be installed
--> Processing Dependency: libXpm.so.4()(64bit) for package: gd-2.0.35-26.el7.x86_64
---> Package gperftools-libs.x86_64 0:2.4-5.el7 will be installed
--> Processing Dependency: libunwind.so.8()(64bit) for package: gperftools-libs-2.4-5.el7.x86_64
---> Package libxslt.x86_64 0:1.1.28-5.el7 will be installed
---> Package nginx-filesystem.noarch 1:1.6.3-7.el7 will be installed
--> Running transaction check
---> Package gperftools-libs.x86_64 0:2.4-5.el7 will be installed
--> Processing Dependency: libunwind.so.8()(64bit) for package: gperftools-libs-2.4-5.el7.x86_64
---> Package libXpm.x86_64 0:3.5.10-5.1.el7 will be installed
--> Finished Dependency Resolution
Error: Package: gperftools-libs-2.4-5.el7.x86_64 (epel)
           Requires: libunwind.so.8()(64bit)
 You could try using --skip-broken to work around the problem
 You could try running: rpm -Va --nofiles --nodigest

{% endhighlight %}

从字面理解，少了一个libunwind.so.8。被gperftools依赖，问题是同样的环境，其他机器安装没这个问题，这个包是自动装的，所以比较奇怪。解决方案有2个：

1. 从其他机器拷贝文件过来，拷贝到 /usr/lib64下面
2. 自己编译libunwind和gperftools，很多帖子提到过，可惜是个坑，没解决。 
3. 自己去找libunwind的rpm包，先装好再装nginx。这个坑爹玩意算是解决了
<ftp://ftp.muug.mb.ca/mirror/centos/7.1.1503/cloud/x86_64/openstack-kilo/common/libunwind-1.1-3.el7.x86_64.rpm>



耽误了一下午时间，应该早点果断下手
