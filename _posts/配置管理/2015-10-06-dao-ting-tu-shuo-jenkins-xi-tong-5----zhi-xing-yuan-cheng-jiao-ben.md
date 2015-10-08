---
layout: post
title: "道听途说Jenkins系统5 - 执行远程脚本"
description: "如何执行远程脚本"
category: "配置管理"
modified: 2015-10-06 21:09
tags: "jenkins 远程脚本 ssh"
---
{% include JB/setup %}
官方参考 <https://wiki.jenkins-ci.org/display/JENKINS/Publish+Over+SSH+Plugin>

# 1、使用插件

 通过publish over sh插件可以解决执行远程命令个问题
 本质上还是执行一个脚本，放在远程可以减少点复杂度，每个脚本各管各的
 
# 2、前置配置

为了能使用key可以顺利执行，需要在目标服务器添加对key的认证，简单说就是对方把自己的key认可为认证过的key。
### 2.1 生成key文件
如果没有key文件，可以生成一个key文件。

{% highlight bash %}  
ssh-keygen -t rsa -b 4096 -C "xx@xx.xx"  
{% endhighlight %}
这里可以设置key的位置，和密码，密码可以为空

### 2.2 上传key文件

上传到目标服务器  
{% highlight bash %}  
scp -P xx ~/.ssh/id_rsaxxxx.pub root@服务器:/目标路径/ 
{% endhighlight %}  
这里如果端口是22，就不要加-P

### 2.3 添加到认证

登录到目标服务器。
{% highlight bash %} 
cat /刚刚上传的文件名 >>~/.ssh/authorized_keys
{% endhighlight %}  
这样就把我们的公钥合并到authorized_keys。  

### 2.4 测试

{% highlight bash %}  
ssh -p 端口好 -i key文件 用户名@服务器  
{% endhighlight %}

如果正常就可以了。如果有问题，可以通过另外的参数来调试.  
{% highlight bash %}  
ssh -i key文件 -vvvvvvvvv -T git@服务器   
{% endhighlight %}   
这里的v个数根据情况定，多点调试信息就全一点。
它会列出完整的过程，如果.ssh下面有config文件，它会先去匹配里面的内容。
 
# 3、全局配置
安装完插件以后，在全局配置里面，会有一个Publish over SSH区段。
里面设置key相关的信息。

* key配置
	这里的key是用private key。  
	key相关的配置项有3个，
	* Path to Key指key的文件路径
	* Key表示key的内容。用key和path to  key是一样的
	* Passphrase 表示key的密码。可以为空
* SSH Servers
	可以可以设置多个服务器。
	* Hostname， 服务器地址
	* Username， 用户名
	* Remote Directory，远程登录上的末日地址  
	高级选项 
	* Port， 端口号。 
	前面的key是全局的，针对不同的服务器，可以设置自己的key。
	
# 4、项目配置

在项目的Add Pre—build Step和Add Post—Build Step里面会有一个选项
Send Files or Exeucte commands over ssh

按照惯例，这里还可以对服务器单独设置key。除此之外还可以设置重试次数（以及相互之间的时间间隔）

在Transfers里面，有2个主要的内容：

* Transfer Set Source Files
  要传输的文件，如果有多个文件，用逗号分隔
* Remove prefix
  删除文件名前缀。如target/deployment/images/**/ —> target/deployment
* Remote Directory
  远程文件夹名
* Exec Command
  要执行的命令。就是一个命令。  
  **通常设置这个就够了，手工传一个上去**  
  在高级里面还有些设定，比如哪些文件不执行。文件夹格式，运行超时时间等等
  
# 5、命令执行
这里的命令主要作用是停止tomcat，删除原来的war，拷贝新war到指定路径，启动tomcat。这个过程是可控的，如果中间出现异常，jenkins会侦测到。