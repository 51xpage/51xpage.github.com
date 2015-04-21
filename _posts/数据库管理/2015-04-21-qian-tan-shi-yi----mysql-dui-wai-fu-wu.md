---
layout: post
title: "浅滩拾遗 - mysql对外服务"
description: "设置mysql对外服务"
category: "数据库管理"
modified: 2015-04-21 19:45
tags: "mysql 对外服务 linux 防火墙"
---
{% include JB/setup %}
## 防火墙设置
mysql的默认端口是3306端口，修改iptables文件
{% highlight bash %}  
vi /etc/sysconfig/iptables
{% endhighlight %}

`
-A IN_public_allow -p tcp -m tcp --dport 3306 -m conntrack --ctstate NEW -j ACCEPT
`

据说需要要在

`
-A RH-Firewall-1-INPUT -j REJECT –reject-with icmp-host-prohibited
`

之前，否则可能导致规则不生效

重启防火墙
{% highlight bash %}  
service iptables restart
{% endhighlight %}	

## mysql设置
可能方法很多，最根本原因不清楚，不过目前更新用户表  
1. 登录mysql  
{% highlight bash %}
mysql -r root -p  
{% endhighlight %}

2. 查看user表
{% highlight sql %}
select user,host from mysql.user;
{% endhighlight %}

||user     || host                  ||  
||---------|| --------------------- ||
|| root    || %                     ||  
|| root    || 127.0.0.1             ||  
|| root    || ::1                   ||  
||         || localhost             ||  
 
确保用户的host有%就可以了