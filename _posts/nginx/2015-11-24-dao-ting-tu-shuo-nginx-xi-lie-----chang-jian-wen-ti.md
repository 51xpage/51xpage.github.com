---
layout: post
title: "道听途说nginx系列 - 常见问题"
description: "nginx问题记录"
category: "nginx"
modified: 2015-11-24 16:46
tags: "nginx"
---
"test-jb-setup"

# 1、403报错
 可能性很多，有一个可能文件权限不对。没有r权限
 
# 2、invalid PID number ""
  启动报这个错，现在的处理办法很简单，直接执行一个命令

{% highlight bash %}  
  nginx -c /etc/nginx/nginx.conf  
{% endhighlight %} 

下面是一大段解释 

issued a nginx -s stop and after that I got this error when trying to reload it.
[error]: invalid PID number “” in “/var/run/nginx.pid”
That /var/run/nginx/pid file is empty atm.
What do I need to do to fix it?
nginx -s reload is only used to tell a running nginx process to reload its config. After a stop, you don't have a running nginx process to send a signal to. Just run nginx (possibly with a -c /path/to/config/file)

# 3、隐藏nginx版本号

在nginx.conf里面设置配置  
{% highlight bash %}  
http {  
……  
server_tokens off;  
……  
}  
{% endhighlight %} 
