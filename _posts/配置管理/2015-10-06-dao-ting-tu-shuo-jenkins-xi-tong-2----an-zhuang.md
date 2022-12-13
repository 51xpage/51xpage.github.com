---
layout: single
title: "道听途说Jenkins系统2 - 安装"
description: "如何安装jenkins，几种安装方式"
category: "配置管理"
modified: 2015-10-06 21:06
tags: "jenkins "
---
{% include JB/setup %}
# 1、概述
jenkins的官方网站是<https://jenkins-ci.org/> 上面有详细的安装方式介绍
Jenkins就是一个war文件，通过官网下载war包即可。
而各个平台的不同安装方式也主要是把这个war下载下来。Jenkins支持的平台很多，现在也支持Docker的方式来做。
# 2、在线安装
如果是在CentOS下，可以通过yum来安装

{% highlight bash %}    
 wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo  
 rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key  
 yum install jenkins  
 {% endhighlight %}  
 
 其他的环境也是类似。 
 这样安装完成以后启动是比较简单的。直接通过service命令即可
 
{% highlight bash %}    
 service jenkins start/stop/restart  
 {% endhighlight %} 
 
# 3、离线安装

但是用这个方法我居然一直没启动成功。装上去放了很久就放弃了。报错，官方说是没有装Java的原因。 
 
 {% highlight bash %}  
 Starting jenkins (via systemctl):  Job for jenkins.service failed. See 'systemctl status jenkins.service' and 'journalctl -xn' for details.
                                                           [FAILED]
                                                           {% endhighlight %}  

这个问题就不纠结了。主要还是因为这个服务器上放了很多服务，实在不想来一个就起一个tomcat。所以想着既然是war，应该可以直接用吧
所以就把war放到webapps下了  
 {% highlight bash %} 
wget http://mirrors.jenkins-ci.org/war/latest/jenkins.war  
{% endhighlight %}  

不借助tomcat，还有一种方式可以使用，即  
 {% highlight bash %} 
java -jar jenkins.war --httpPort=9090
{% endhighlight %}  

# 4、基本使用
不管用上面方式安装完成以后，通过web就可以访问了。
默认情况下它并不需要登录直接可以使用。

# 5、文件结构
我们可以看到，配置都在~/.jenkins里面，其中

* workshop
	里面应该是当前代码
* jobs
	里面放编译好的历史结果
	/root/.jenkins/jobs/jeecg/modules/包名$项目名
	
	这里还有项目的配置文件，即文件夹下面的 config.xml


