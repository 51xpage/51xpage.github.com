---
layout: post
title: "道听途说Linux系列14 - 端口使用情况查看"
description: "Linux下查看端口使用情况"
category: "服务器管理"
modified: 2016-02-16 14:42
tags: "linux netstat ss 端口"
---
{% include JB/setup %}

很多情况下，我们需要查看端口使用情况，知道端口是否使用，什么进程在使用，流量等等，有几个命令可以查看

# 1、netstat
它的参数很多，目前用得比较多是 lntp
其中 
l表示正在监听的端口
n表示尽量显示数字
t表示只显示tcp，对应的udp为u
p表示进程id，需要root权限

{% highlight bash %}
netstat -lntp  
{% endhighlight  %}

# 2、lsof

{% highlight bash %}
lsof -i:3306
{% endhighlight  %}

显示3306端口被谁占用

# 3、ss

{% highlight bash %}
ss -tnl  
{% endhighlight  %}
查看监听地址

# 4、iftop

需要另外装，可以直接看各个端口的流量情况

以后把几个工具结合起来写吧，还有iftop等等