---
layout: post
title: "道听途说Linux系列7 - sftp无法使用解决示例"
description: "解决sftp无法使用，引申出文件权限的解决办法"
category: "服务器管理"
modified: 2015-11-30 15:01
tags: "chmod lsattr chattr"
---
{% include JB/setup %}

# 1、问题提出

一个用了很久的服务器，最近发现无法用sftp连接了，但是scp和ssh还可以连，比较奇怪。按照网上的说法

{% highlight bash %}    
service sshd restart  
{% endhighlight %}  
无效

# 2、解决过程

* 测试连接过程

{% highlight bash %}  
sftp -v -P 1022 root@xxxxxx  
{% endhighlight %} 

最后发现返回是  

{% highlight bash %}  
debug1: Exit status 126  
Connection closed  
{% endhighlight %} 

有资料提示可能是权限问题，

* 检查权限

到宿主机，找到  

{% highlight bash %}  
vim /etc/ssh/sshd_config  
{% endhighlight %} 

找到SubSystem  这里指定了 sftp的服务器地址

{% highlight bash %}  
Subsystem       sftp    /usr/libexec/openssh/sftp-server  
{% endhighlight %} 

通过ll命令查看权限

{% highlight bash %}  
ll /usr/libexec/openssh/sftp-server  
{% endhighlight %} 

发现没有任何权限，

{% highlight bash %}  
chmod +x /usr/libexec/openssh/sftp-server   
{% endhighlight %} 

提示权限不足
甚至 cp，mv等等命令都不行，


* 临时方案

从其他服务器拷贝一个sftp-server过来，改个名字，修改sshd_config中的地址，暂时搞定了

* 再起变化

今天要安装的时候，发现wget也提示没有权限

而且chmod等等都无效，没有任何权限，相比是被攻击了，这tm算降维攻击吗？快快成长呀

# 3、最终方案

终于在网上找到个资料，提到另外2个命令 `lsattr`和`chattr`  
{% highlight bash %}  
lsattr /usr/libexec/openssh/sftp-server  
{% endhighlight %} 

发现有一个i的标记。这个标记文件只读，可以通过 

{% highlight bash %}  
chattr -i /usr/libexec/openssh/sftp-server  
{% endhighlight %} 

问题是这个文件不存在，然后通过另外一个服务器把这个文件拷贝到

{% highlight bash %}  
scp /usr/bin/chattr root@xxxxxx:/usr/bin  
{% endhighlight %} 

然后再chmod

{% highlight bash %}  
chmod +x /usr/bin/wget  
{% endhighlight %} 

# 4、参考

chattr 主要就是i的属性,表示只读
用 + 和 -号来增加或者删除属性

* = ：更新为指定参数设定。
* A：文件或目录的 atime (access time)不可被修改(modified), 可以有效预防例如手提电脑磁盘I/O错误的发生。
* S：硬盘I/O同步选项，功能类似sync。
* a：即append，设定该参数后，只能向文件中添加数据，而不能删除，多用于服务器日志文件安全，只有root才能设定这个属性。
* c：即compresse，设定文件是否经压缩后再存储。读取时需要经过自动解压操作。
* d：即no dump，设定文件不能成为dump程序的备份目标。
* i：设定文件不能被删除、改名、设定链接关系，同时不能写入或新增内容。i参数对于文件 系统的安全设置有很大帮助。
* j：即journal，设定此参数使得当通过mount参数：data=ordered 或者 data=writeback 挂 载的文件系统，文件在写入时会先被记录(在journal中)。如果filesystem被设定参数为 data=journal，则该参数自动失效。
* s：保密性地删除文件或目录，即硬盘空间被全部收回。
* u：与s相反，当设定为u时，数据内容其实还存在磁盘中，可以用于undeletion。
各参数选项中常用到的是a和i。a选项强制只可添加不可删除，多用于日志系统的安全设定。而i是更为严格的安全设定，只有superuser (root) 或具有CAP_LINUX_IMMUTABLE处理能力（标识）的进程能够施加该选项。