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



最近尝试了下VPN的架设，期间遇到的一些问题在此做个记录和总结：

1.pptpd已启动运行，但不能正常连接，查看messages发现以下记录：


MGR: connections limit (100) reached, extra IP addresses ignored

MGR: Manager process started

MGR: Maximum of 100 connections available

   通过搜索，查得解决方法如下：

   a.打开配置文件/etc/pptpd.conf，注释掉其中的logwtmp，如下所示：


    # TAG: logwtmp

    #       Use wtmp(5) to record client connections and disconnections.

    #

    #logwtmp

   b.确保在iptables打开了1723端口：

       -A INPUT -p tcp -m state --state NEW -m tcp --dport 1723 -j ACCEPT

   通过以上几步应该可以解决问题。



2.VPN可以连接成功，但不能正常上网，messages中记录如下：

       Cannot determine ethernet address for proxy ARP

   该问题主要出在没有相关的转发规则。需要进行如下配置：

   a.打开配置文件/etc/sysctl.conf，修改配置项net.ipv4.ip_forward为1：    

    # Controls IP packet forwarding

    net.ipv4.ip_forward = 1

       该配置项用于允许ip转发。

   b.还需在iptables中加入NAT转换：

       iptables -t nat -A POSTROUTING -s 192.168.0.0/255.255.255.0 -j SNAT --to-source 192.168.0.88

       其中192.168.0.0/255.255.255.0为VPN的内部网络，192.168.0.88当然就是服务器的地址了。
       
       tail -f /var/log/ppp.log