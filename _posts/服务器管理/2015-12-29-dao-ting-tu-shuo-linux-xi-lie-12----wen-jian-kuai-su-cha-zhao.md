---
layout: single
title: "道听途说Linux系列12 - 文件快速查找"
description: "Linux下文件查找技巧"
category: "服务器管理"
modified: 2015-12-29 16:01
tags: "linux find 文件 查找 最大"
---
{% include JB/setup %}

网络收集，侵删

* 查找指定文件夹最大的文件

 {% highlight bash %}   
du -a / | sort -n -r | head -n 10
{% endhighlight %} 

 我用来查文件夹为什么大了

* 查找大100M的文件

 {% highlight bash %}   
 find /dir -size +100M -exec ls -lh {} ＼;
 {% endhighlight %} 
 
* 删除大于50M文件

 {% highlight bash %}   
 find /var/mail/ -size +50M -exec rm {} ＼;
 {% endhighlight %} 

* 
======
代码示例:

清空一些文本文件类的东西：
 

代码示例:
echo "" > /www.jbxue.com /xxx.log
此命令能与“echo > /var/log/big.log”达到相同效果，不过，命令执行后，需要用“Ctrl + d”结束

clear > /opt/log/big.log
此命令会把big.log文件内容清空，而不删除文件

同样的效果，用true、flase、“:”等也能实现清空文件内容，而不删除文件的效果
 

代码示例:
true > /opt/log/big.log
flase > /opt/log/big.log
: > /opt/log/big.log
若想删除文件，只需利用rm命令即可。
 

代码示例:
rm -f  /opt/log/big.log
如果想排序文件夹和文件，可以使用。
 

代码示例:
du -s * | sort -nr | head
两个更简单的方法，用于清空文件内容： 
 

cat /dev/null > 要清空的文件
>要清空的文件
以上命令请谨慎使用，避免清空重要文件。


====

linux下批量删除空文件（大小等于0的文件）的方法

find . -name "*" -type f -size 0c | xargs -n 1 rm -f

用这个还可以删除指定大小的文件，只要修改对应的 -size 参数就行，例如：

find . -name "*" -type f -size 1024c | xargs -n 1 rm -f

就是删除1k大小的文件。（但注意不要用 -size 1k，这个得到的是占用空间1k，不是文件大小1k的）。

如果只要删除文件夹或者名字连接等，可以相应的改 -type 参数，具体细节见 man find。


grep -v '^$' regular_express.txt | grep -v '^#'

======
除了这些内容，还有几个和时间相关的参数很有用

ctime的意思是change time，文件状态最新改变的时间。是文件的status change time，何为文件的status呢？
我们都知道文件有一些个基本的属性，权限，用户，组，大小，修改时间等，只要是这些信息变化了，那么ctime都会发生变化，
所以上面修改文件内容时为何ctime会变化，因为其mtime已经变化了，mtime也是文件状态的一个。
http://blog.itpub.net/26675752/viewspace-1058878/