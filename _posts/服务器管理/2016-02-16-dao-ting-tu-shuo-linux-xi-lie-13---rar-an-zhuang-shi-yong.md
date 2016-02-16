---
layout: post
title: "道听途说Linux系列13 - rar安装使用"
description: "Linux下rar安装使用"
category: "服务器管理"
modified: 2016-02-16 14:09
tags: "linux rar 解压缩"
---
{% include JB/setup %}

# 概述

   大多数情况下使用gunzip和tar，鲜有需要rar的时候，正好碰到，记录一下。
   
# 1、前置安装

{% highlight bash %}  
yum -y install libstdc++
yum -y install libstdc++.i686  
{% endhighlight %} 

# 2、安装
{% highlight bash %}  
wget http://www.rarsoft.com/rar/rarlinux-3.9.3.tar.gz   
tar -xvf rarlinux-3.9.3.tar.gz   
cd rar   
make    
cp rar unrar /usr/local/bin  
cp rarfiles.lst /etc  
cp default.sfx /usr/local/lib   
{% endhighlight %}  

# 3、使用
{% highlight bash %}  
#test.rar 到当前目录  
rar x test.rar   
# 把test001目录压缩为 test.rar  
rar test.rar ./test001/   
{% endhighlight %} 

# 4、场景问题

* rar: /lib/i686/nosegneg/libc.so.6: version `GLIBC_2.7' not found (required by rar)

解决办法：
{% highlight bash %}  
cp rar_static /usr/local/bin/rar  
{% endhighlight %}  


