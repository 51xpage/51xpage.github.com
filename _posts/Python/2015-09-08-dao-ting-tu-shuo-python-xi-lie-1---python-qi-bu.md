---
layout: single
title: "道听途说Python系列1 - Python起步"
description: "Python起步"
category: "Python"
modified: 2015-09-08 10:39
tags: "爬虫 Python PyCharm"
---
{% include JB/setup %}

# 缘起
很久以前知道有这个语言，一直没有仔细研究涉及，只知道是一个脚本语言，想着和Javascript差不多的语言。第一次有些触动是因为据说OpenStack是用Python语言写的。后来零零星星据说是一种胶水语言，可以黏合很多系统，另外说是擅长做爬虫。对于爬虫的理解，我一直是用Delphi的IdHttp来请求抓数据，并不认为有所谓擅长不擅长之说，这个问题现在还没有特别想的清楚，以后慢慢体会吧。再后来据说Python是Google的4大语言之一。然后有一个爬虫的需求，所以就用Python尝试。下面是一些学习的点滴，希望这个系列可以成为Python的一条入门之路。

对于一个语言而言，生态是很重要的，语法本身而言的影响，和整个生态而言，是微不足道的。想起以前VCL和MFC的争论，VCL的崛起和衰落，这也许也是原因吧。

# 1、基本操作

Python在Linux和Mac上是内置的，通常都是2.x版本。也就是说在终端之间输入 python就可以执行了。如果只用这个版本，也就不用安装了。使用也很简单。

* 简单处理

在终端输入 python 可以直接进入python环境，可以看到python版本号和一个输入符号<<<。

{% highlight bash %}   
python

Python 3.5.0 (v3.5.0:374f501f4567, Sep 12 2015, 11:00:19)  
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin  
Type "help", "copyright", "credits" or "license" for more information.  
>>> 1+2  
3  
>>> print("hello")  
hello

{% endhighlight %}  

从上面我们可以看到，要简单执行一个操作是很容易的，python本身也提供了很多方法，比如数学方法等等

* 运行脚本
实际项目中，我们一般的理念，总得有个什么形式来做发布什么的，windows的exe，java的war等等，总不能在脚本里面这么跑吧。目前的做法是通过python命令来做。比如：
python xxxx.py

这样就可以了。但是这样做会依赖当前会话。如果是ssh，关闭窗口的时候，python也终止了。
所以可以通过其他的工具协助来做。比如：

{% highlight bash %}   
nohup python xxx.py &
{% endhighlight %}   

#2、 python版本升级

上面提到的都是基于现有python版本的。如果需要替换，特别是这个时间点上，2.x和3.x版本并存，而且相互并不兼容，从长远看，一定是往前发展的。所以就存在替换版本的问题。下面以centos 7为例，介绍如何升级。

### 2.1、前置安装

安装方式是源码安装，版本为3.4.3。需要前置很多包，否则在编译阶段会出错

{% highlight bash %} 
yum install readline-devel sqlite-devel  
yum install openssl openssl-devel  
yum install zlib zlib-devel  
yum install gdbm-devel  
yum install xz-devel bzip2-devel    
yum install tk-devel

{% endhighlight %}

### 2.2、介质下载

{% highlight bash %}  
	wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz  
{% endhighlight %}  	
	
### 2.3、开始安装
 	
 这里建议把make和 make install 分开来执行，可以看下过程有什么问题，缺什么强制安装的东西
 	
{% highlight bash %}  	
 	mkdir /usr/local/python3.4.3  
    tar -vxf Python-3.4.3.tgz  
    ./configure --prefix=/usr/local/python3.4.3    
    make  
    make install  
{% endhighlight %}  
    
#2.3、 配置修改

因为要保证2个环境并存，所以把原来/usr/bin/python 替换掉，并把pip也替换掉

{% highlight bash %} 
	mv /usr/bin/python /usr/bin/python_old   
	ln -s /usr/local/python3.4.3/bin/python3 /usr/bin/python  
	ln -s /usr/local/python3.4.3/bin/pip3 /usr/bin/pip
{% endhighlight %}

# 2.4、检查版本

{% highlight bash %}  
python --version  
{% endhighlight %} 

# 2.5、yum修改

centos的yum是基于系统的python做的，是基于python 2.x，所以升级以后会无法使用 python
因为python版本调整过了，所以需要修改yum配置  

{% highlight bash %}  
vim /usr/bin/yum    
vim /usr/libexec/urlgrabber-ext-down
{% endhighlight %}     

第一行修改成 
{% highlight bash %}  	
#!/usr/bin/python2  
{% endhighlight %}  

否则会有报错  
{% highlight bash %}  
 	except KeyboardInterrupt, e:
{% endhighlight %}  
 	
# 2.6 卸载python 3.4

有安装也对应有卸载。下面是Mac的脚本，供参考。  

{% highlight bash %}  
   sudo rm -r /Library/Frameworks/Python.framework /Applications/Python\ 3.* /Library/Receipts/Python*-3.*.pkg  
   sudo rm -Rfv /Library/Frameworks/Python.framework/ /Applications/Python\ 3.*/   
   cd /usr/local/bin/  
   sudo rm -fv 2to3 2to3-3.* idle3 idle3.* pydoc3 pydoc3.* python3 python3-32 python3-config python3.* python3.*-32 python3.*-config python3.*m python3.*m-config pythonw3 pythonw3-32 pythonw3.* pythonw3.*-32 /Developer/Documentation/Python/Reference\ Documentation\ 3.*  
{% endhighlight %}  

因为自己现在用的是 zsh，如果有调整，原来放在 .bash_profile里面的，需要改成放到.zshrc。

# 3、安装python包

目的是为了安装别人做好的库，Package。安装通常是通过pip命令来做。pip会随着python的安装一起安装。

#3.1、 通过pipy

这个可以理解为yum， apt-get 类似的命令，它会去pypi找一个中央库，然后从那里下载。简单方便

{% highlight bash %}  	
pip install flash-restful    
{% endhighlight %}  

#3.2、 依赖安装

对于已经做好的一个项目，里面会用到很多依赖的外部python包，这个时候可以通过一个文本文件列出所有依赖的文件。通过-r参数来安装，如

{% highlight bash %}  
pip install -r requirements.txt  
{% endhighlight %}  

这个文件可以自己写，也可以通过工具生成。

{% highlight bash %} 
redis == 2.10.5
requests == 2.8.1
{% endhighlight %}  

{% highlight bash %}  
$ pip install pipreqs
$ pipreqs 项目路径  
{% endhighlight %}  

#3.3、本地源码安装

 没装过

#3.4、允许外部

{% highlight bash %} 
pip install --allow-external mysql-connector-python mysql-connector-python  
{% endhighlight %}  
  
  不加 --allow-external 会提示，照着提示也能搞定
 
 
#3.4、在线安装

{% highlight bash %}  
pip install -e "git://github.com/FelixLoether/flask-uploads#egg=Flask-Uploads  
{% endhighlight %}  

通过这样的方式，就可以安装最新的版本，应该也算是源码安装吧
  
#3.5、 升级pip
  
{% highlight bash %} 
pip install --upgrade pip    
{% endhighlight %}   
  
# 3.6、 其他pip参数

可以通过帮助看到，一般是 list看安装过的程序，通过upgrade升级
 

#4、 开发工具选择

工具很多，基于上面的描述，我们用普通的文本编辑器就够了，对于生产力工具来说。当然还是推荐使用成熟的IDE工具，推荐使用PyCharm