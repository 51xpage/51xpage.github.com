---
layout: post
title: "道听途说Linux系列 6 - shell中使用nohup"
description: "linux脚本中nohup需要手动回车问题"
category: "服务器管理"
modified: 2015-11-24 16:34
tags: "linux shell nohup"
---
{% include JB/setup %}

# 问题提出
   
   可以在命令行执行脚本的方法很多，个人接触的主要是2种
 {% highlight bash %}    
   echo xxx |at now  
 {% endhighlight %}

{% highlight bash %}  
   nohup  sh   catalina.sh  run &  
{% endhighlight %}
   
   前面的方案不一定都有效，后面以nohup启动服务可以在终端关闭后保证Linux环境下的服务在后台继续运行，通常在终端执行时需要执行一下回车键才能保证命令进行，为了保证nohup在脚本中被成功调用执行，需要在脚本中增加回车的符，否则命令执行不成功  

# 解决方案


以下是以nohup方式启动tomcat的脚本  
 
{% highlight bash %}   
 
#!/bin/bash  
  
str=$"/n"  
  
cd /SAPP/tomcat-admin/bin  
  
nohup  sh   catalina.sh  run &  
  
sstr=$(echo -e $str)  
  
echo "$sstr 
{% endhighlight %}  

精华就是最后那一点点东西了
