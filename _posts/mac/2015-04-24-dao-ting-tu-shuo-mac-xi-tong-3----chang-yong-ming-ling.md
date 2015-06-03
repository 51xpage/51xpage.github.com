---
layout: post
title: "道听途说mac系统3 - 常用命令"
description: "mac下的常用命令"
category: "mac"
modified: 2015-04-24 16:39
tags: "mac 命令"
---
{% include JB/setup %}
# Mac 常用命令  
## 1、远程文件拷贝
{% highlight bash %} 
   scp -r root@xx.xx.xx:/etc/nginx/ ./
{% endhighlight  %} 

其中：
  
* -r 表示递归拷贝子文件夹
* 前面是源路径，后面是目标路径yohi
   
## 2、文件数量大小统计
#### 查看某文件夹下文件的个数
{% highlight bash %}  
ls -l |grep "^-"|wc -l 
{% endhighlight  %} 

* ls -l  
长列表输出该目录下文件信息(注意这里的文件，不同于一般的文件，可能是目录、链接、设备文件等)

* grep "^-"  
这里将长列表输出信息过滤一部分，只保留一般文件，如果只保留目录就是 ^d

* wc -l  
统计输出信息的行数，因为已经过滤得只剩一般文件了，所以统计结果就是一般文件信息的行数，又由于一行信息对应一个文件，所以也就是文件的个数。 

 

#### 查看文件夹大小
查看当前文件夹大小  
{% highlight bash %}  
 du -sh  
{% endhighlight  %} 

统计当前文件夹(目录)大小，并按文件大小排序  
{% highlight bash %}  
du -sh * | sort -n 
{% endhighlight  %} 

查看指定文件大小   
{% highlight bash %}  
du -sk filename 
{% endhighlight  %} 

#### 查看历史命令
{% highlight bash %}  
 history |grep 关键字
{% endhighlight  %} 

再次执行历史命令，感叹号后面加命令编号
{% highlight bash %}  
 !234
{% endhighlight  %} 

ctrl + R 可以模式搜索历史命令
