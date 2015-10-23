---
layout: post
title: "道听途说linux系统4 - pptpd配置"
description: "aws下配置pptpd代理服务器"
category: "服务器管理"
modified: 2015-10-23 16:49
tags: "pptpd proxy linux aws"
---
{% include JB/setup %}

#问题提出

# 2 配置过程
### 2.1 安装PPTPD
{% highlight bash %}   
sudo apt-get install pptpd
{% endhighlight %}

### 2.2 配置/etc/pptpd.conf
{% highlight bash %}   
localip 192.168.0.1  
remoteip 192.168.0.234-238,192.168.0.245  
{% endhighlight %}

### 2.3 配置/etc/ppp/options
{% highlight bash %}   
ms-dns 8.8.8.8  
ms-dns 8.8.4.4  
ms-dns 114.114.114.114  
{% endhighlight %}

### 2.4 配置日志位置

修改**/etc/ppp/options**，增加  
{% highlight bash %}   
logfile /var/log/ppp.log  
{% endhighlight %}

### 2.5 配置连接数
改上面的那个文件，这里的范围就表示连接的用户数  
248 - 234 = 16    
{% highlight bash %}   
remoteip 192.168.0.234-248,192.168.0.245  
{% endhighlight %}

### 2.6 配置/etc/ppp/chap-secrets
{% highlight bash %}   
test pptpd passw0rd * 
{% endhighlight %}

这里最后 * 表示连接的用户地址，表示任意

### 2.7 修改/etc/sysctl.conf
增加  
{% highlight bash %}   
net.ipv4.ip_forward=1  
{% endhighlight %}

重载
{% highlight bash %}   
sysctl -p  
{% endhighlight %}

### 2.8 启动
{% highlight bash %}   
service pptpd restart  
service pppd-dns restart  
{% endhighlight %}

#AWS配置
防火墙是通过安全组做的，在安全组策略里面设置入站和出站规则

在系统里面设置iptables啥啥啥的，纯属瞎折腾
