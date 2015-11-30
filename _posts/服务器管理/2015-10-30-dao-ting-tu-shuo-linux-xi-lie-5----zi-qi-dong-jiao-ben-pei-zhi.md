---
layout: post
title: "道听途说Linux系列5 - 自启动脚本配置"
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
# chkconfig: 2345 10 90 
# description: srv

{% endhighlight %}    
 
   `service svr.sh does not support chkconfig`
   
   如果不加chkconfig会报错，description倒没关系
   
   **另外有一点，系统默认以 start 参数启动，所以如果脚本里面写了start函数，那就需要让参数引导过来，如果没有函数，反正它就整体执行了呗**
   
   
	   其中2345是默认启动级别，级别有0-6共7个级别。

		等级0表示：表示关机 　　

		等级1表示：单用户模式 　　

		等级2表示：无网络连接的多用户命令行模式 　　

		等级3表示：有网络连接的多用户命令行模式 　　

		等级4表示：不可用 　　

		等级5表示：带图形界面的多用户模式 　　

		等级6表示：重新启动

		10是启动优先级，90是停止优先级，优先级范围是0－100，数字越大，优先级越低。
		
4. 常见问题

* 脚本调试
	
	脚本在运行之前可以通过命令来测试语法问题
	
	`sh -n xxxxx`  
	
* 服务调试
	
	`systemctl status srv.service  `  
	`journalctl -xn`  
	通过这两个命令可以看下服务出现了什么错误
	
* 修改服务脚本

	`systemctl daemon-reload  `   
	修改完以后需要通过这个脚本重新加载
	
* 退出问题
	
	如果脚本最后不exit 0，系统会任务我们失败了

* syntax error:unexpected end of file
 	

   
   参考 <http://www.cnblogs.com/image-eye/archive/2011/10/26/2220405.html>
   <https://www.ibm.com/developerworks/cn/linux/kernel/startup/>