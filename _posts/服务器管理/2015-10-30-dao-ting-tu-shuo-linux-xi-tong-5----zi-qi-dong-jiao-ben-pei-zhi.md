---
layout: post
title: "道听途说linux系统5 - 自启动脚本配置"
description: "linux下自启动脚本配置"
category: "服务器管理"
modified: 2015-10-30 13:43
tags: "linux 自动启动 脚本"
---
{% include JB/setup %}
# 问题提出
  
  因为服务器要启动的内容比较多，所以自己建立了一个脚本来启动各个服务。
  为了更加方便，希望做成自动启动的服务。但是网上搜了一大把发现都没有特别合适的方案。
  
  **当然，这个sh文件是有执行权限的。**
  
# 尝试方案

1. /etc/rc.d/rc.local

	直接修改这个文件

	* 添加了执行的sh文件路径，失败
	* 先cd到对应的路径，失败
	* 前面加 sh  xxxx.sh，失败
	* 前面加 /bin/bash xxx.sh， 失败

2. /etc/rc.d/init.d  
	
	失败

3. chkconfig

	`error reading information on service startup.sh: No such file or directory`  
	

# 解决方案

   如果不在 /etc/rc.d/init.d 文件夹下 会报错,所以文件放这里来是第一步。
   {% highlight bash %}  
   chkconfig --add xxxx
   
   
   {% endhighlight %}    
   
   删除用 del，覆盖用 override参数即可
   
   然后考虑格式的问题。它需要的是固定格式。所以这个文件开头部分需要几个内容
  
{% highlight bash %}  

#! /bin/bash
#
# chkconfig 234 xxx

{% endhighlight %}    

   这个是扯淡的，可能是因为刚开始没chkconfig成功，所以整成服务的方式了。  
   
   **另外有一点，系统默认以 start 参数启动，所以如果脚本里面写了start函数，那就需要让参数引导过来，如果没有函数，反正它就整体执行了呗**
   
   参考 <http://www.cnblogs.com/image-eye/archive/2011/10/26/2220405.html>
   <https://www.ibm.com/developerworks/cn/linux/kernel/startup/>