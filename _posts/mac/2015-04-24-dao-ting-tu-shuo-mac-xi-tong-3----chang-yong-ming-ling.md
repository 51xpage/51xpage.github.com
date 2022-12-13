---
layout: single
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
* 前面是源路径，后面是目标路径
* 如果对方默认端口不是22，需要在前面指定。如

{% highlight bash %}   
   scp -P 722 -r root@xx.xx.xx:/etc/nginx/ ./  
{% endhighlight  %}    
这里的P要大写

   
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

## 3、 查看历史命令
{% highlight bash %}  
 history |grep 关键字
{% endhighlight  %} 

再次执行历史命令，感叹号后面加命令编号
{% highlight bash %}  
 !234
{% endhighlight  %} 

ctrl + R 可以模式搜索历史命令

## 4、 查看文件大小
语法：wc [选项] 文件…

说明：该命令统计给定文件中的字节数、字数、行数。如果没有给出文件名，则从标准输入读取。wc同时也给出所有指定文件的总统计数。字是由空格字符区分开的最大字符串。

该命令各选项含义如下：

　　- c 统计字节数。
　　- l 统计行数。
　　- w 统计字数。
　　
{% highlight bash %}  
 wc -lcw 文件名
{% endhighlight  %} 　　

可以和find命令结合，如
{% highlight bash %}  
 find / -name xxx|wc -lcw
{% endhighlight  %} 　

## 5、 查看文件部分内容
{% highlight bash %}   
   cat 文件名 | tail -n +起始行 | head -n 总显示行数  
{% endhighlight  %} 
 
{% highlight bash %} 
   cat 文件名 | head -n 终止行 | tail -n +起始行  
{% endhighlight  %} 

## 6、搜索文件内容

* grep 

{% highlight bash %}   
   grep 搜索正则  文件名  
{% endhighlight  %}  

## 7、查看文件日期

{% highlight bash %}   
   stat 文件名  
{% endhighlight  %}  

{% highlight bash %} 
$ stat data.txt  
  File: ‘data.txt’  
  Size: 32600287        Blocks: 63680      IO Block: 4096   regular file  
Device: ca01h/51713d    Inode: 403585      Links: 1  
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)  
Access: 2015-12-02 10:09:36.381295639 +0800  
Modify: 2015-12-02 01:53:31.011156697 +0800  
Change: 2015-12-02 01:53:31.011156697 +0800  
 Birth: -  
 {% endhighlight %} 

