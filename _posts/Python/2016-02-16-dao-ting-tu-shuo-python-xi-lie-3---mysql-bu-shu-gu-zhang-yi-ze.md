---
layout: post
title: "道听途说Python系列3 - mysql部署故障一则"
description: "Python部署报mysql没有pooling问题解决记录"
category: "Python"
modified: 2016-02-16 15:28
tags: "python attribute mysql.connector pooling"
---
{% include JB/setup %}

# 1、问题描述

  部署2个服务器，CentOS 7，事先都安装过Python 3.4。事先用pip（已经指向到pip3）安装过mysql官方驱动。
  运行的时候报一下错误。
  
  一开始报错是 提示 mysql.connector没有pooling（代码里面用到了）。后来折腾几次变成下面的这个错误了
     {% highlight bash %}  
  >>> import mysql.connector
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/python3.4.3/lib/python3.4/site-packages/mysql/connector/__init__.py", line 41, in <module>
    from .optionfiles import read_option_files
  File "/usr/local/python3.4.3/lib/python3.4/site-packages/mysql/connector/optionfiles.py", line 35, in <module>
    from .fabric import CNX_FABRIC_ARGS
ImportError: cannot import name 'CNX_FABRIC_ARGS'
    {% endhighlight %} 

# 2、解决过程

  发现包都放在  
     {% highlight bash %} 
	/usr/local/python3.4.3/lib/python3.4/site-packages/mysql/connector/fabric
 	{% endhighlight %} 

发现它没有pooling。后来发现是因为根本就没有对应的pooling，而且也没有生成ypc文件，比较奇怪，重新安装了几种方式都不行，还会报错，不知道咋解决的



安装方法如下。

* 方法1
   
   {% highlight bash %} 
  	pip install mysql-connector-python --allow-external mysql-connector-python
   {% endhighlight %} 
    
* 方法2
   {% highlight bash %} 
	/usr/local/python3.4.3/bin/pip3 install mysql-connector-python --allow-external mysql-connector-python
   {% endhighlight %} 

* 方法3
   {% highlight bash %} 
	pip install mysql-connector
   {% endhighlight %} 
    
* 方法4
   {% highlight bash %} 
	pip install mysql-connector-python==2.1.2 --allow-external mysql-connector-python
   {% endhighlight %} 
    
* 方法5
   {% highlight bash %} 
  cd ~/soft
  mkdir mysql-connector-python
  cd mysql-connector-python/
  git clone https://github.com/mysql/mysql-connector-python.git
  cd mysql-connector-python/
  python ./setup.py build
  python ./setup.py install
  {% endhighlight %} 

* 方法6
   {% highlight bash %} 
   pip --upgrade mysql-connector-python --allow-external mysql-connector-python
   pip install --upgrade mysql-connector-python --allow-external mysql-connector-python
   python server.py 
   pip list
   pip remove mysql-connector-python
   pip --help
   pip uninstall mysql-connector-python
    {% endhighlight %}    
    
* 方法7
  
    {% highlight bash %} 
    cd ~/soft
    ll
    rpm -ivh mysql-connector-python
    rpm -ivh mysql-connector-python-2.1.3-1.el7.x86_64.rpm 
    {% endhighlight %} 

* 方法8  
   {% highlight bash %} 
    pip install mysql-connector-python-2.1.3
    pip install mysql-connector-python==2.1.3
    pip install mysql-connector-python --allow-external mysql-connector-python
   {% endhighlight %} 

# 3、最终方案
   最后的最后，通过grep去查正常的那个机器，有没有引用pooling，发现是有的，而且__init__.py也不一样。所有把文件__init__.py都拿过来了，还是报错。
   然后最狠的一招。把整个目录拷贝过来了，好了

# 4、几个心得

* 命令
{% highlight bash %} 
pip search mysql-connector-python
pip search mysql-connector-python --index https://pypi.mirrors.ustc.edu.cn/simple/
{% endhighlight %}  
  
* 判断模块是否安装好了
{% highlight bash %} 
python
>>> import xxxx
调用方法即可
{% endhighlight %}  