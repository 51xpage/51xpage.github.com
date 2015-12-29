---
layout: post
title: "道听途说Linux系列10 - shell脚本编程"
description: "Linux下shell编程基础"
category: "服务器管理"
modified: 2015-12-29 15:50
tags: "linux shell 循环 函数 文件包含"
---
{% include JB/setup %}

shell脚本在运维中非常实用，但是也因为是脚本语言，书写调试等方面都会比较困难。以下记录学习过程中用到的内容。当然下面介绍的应该是基于bash的，曾经用过AIX下面的ksh，不太习惯。

1. 如何编写和运行脚本

   应景，所以shell脚本以sh为扩展名，实际上这个没关系。只要有执行权限即可。
   
   {% highlight bash %} 
   vi xxx.sh  
   chmod +x xxx.sh  
   ./xxx.sh  
    {% endhighlight %} 
   
2. 如何传递参数和获取参数
	
	参数传递比较简单，命令行后面用空格分开就可以，如
	{% highlight bash %}  
	./xxx.sh 参数1  参数2
	{% endhighlight %} 
	
	脚本中如果要使用通过$符号加序号即可获取，如
	param=$1
	
3. 变量使用
4. 字符串
	
	* 拼接字符串
	* 字符串分隔
	
5. 数组

for var11 in ${ arr[@] };

6. 循环
7. 
5. 函数
	
   * 基本形式
   * 返回值
	
6. 文件引用
  
   shell的文件引用目前只了解过一种方式，即
   
   . 文件名
   注意这里的空格

7. 注意事项

    使用变量的时候，不要加空格




shell数组 http://blog.csdn.net/redhat456/article/details/6068409

获取路径名什么的
我使用过的Linux命令之dirname - 截取给定路径的目录部分

http://www.cnblogs.com/sunyubo/archive/2011/10/17/2282047.html
判断文件是否存在

几个坑，因为以前为了代码美观，= 号两头有空格，现在shell公然不支持，




shell 文件包含

参考资料

<http://see.sl088.com/wiki/Shell_%E8%B0%83%E7%94%A8sh%E6%96%87%E4%BB%B6%E9%87%8C%E7%9A%84%E5%87%BD%E6%95%B0>

<http://www.runoob.com/linux/linux-shell-include-file.html>

<http://arganzheng.iteye.com/blog/1174470>

<http://www.cnblogs.com/chengmo/archive/2010/10/17/1853356.html>

shell 返回字符串
http://tinyweb.blog.51cto.com/2462673/982616


<http://www.coder4.com/archives/3853>