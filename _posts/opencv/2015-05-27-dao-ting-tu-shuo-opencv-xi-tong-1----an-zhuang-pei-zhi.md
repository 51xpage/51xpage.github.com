---
layout: post
title: "道听途说opencv系统1 - 安装配置"
description: "只是简单的介绍下干啥用的"
category: "opencv"
modified: 2015-05-27 23:32
tags: "opencv"
---
"test-jb-setup"
# 
# 1、前置条件

* GCC
* CMake
* Git
* GTK
* Python

其他的几个没装，好像也没用到

# 2、代码获取
2种方案

* 通过git获取  
 {% highlight bash %}  
   cd ~/<my_working _directory>
    git clone https://github.com/Itseez/opencv.git
  {% endhighlight %} 
* 直接下载源码  
    主页有下载，直接下载压缩包
    
# 3、cmake
{% highlight bash %} 
cd ~/opencv
mkdir release
cd release
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
{% endhighlight %} 

# 4、编译安装
{% highlight bash %} 
make && make install
{% endhighlight %} 

# 5、常见问题
* ippicv 下载失败  
 2种方法解决：
  * 加参数  
      -D WITH_IPP=OFF
  * 直接从官方网站下载提示信息里面的ippicv文件，放到对应路径，如   
  3rdparty/ippicv/downloads/linux-d80cb24f3a565113a9d6dc56344142f6/
  
  <http://sourceforge.net/projects/opencvlibrary/files/3rdparty/ippicv/>
  
* java.library.path问题
   无法调用自己写的so文件  
   可以修改/etc/profile。导出一个变量 LD_LIBRARY_PATH
   
   可以写个简单程序，确定一下是否可以了
   {% highlight bash %} 
   javac test.java  
   java test    # 这里不要加.class  
   System.setProperty("java.library.path")
   {% endhighlight %} 
   
   通过这个查看，
   
 * glib版本问题
    1. 检查版本
    
     {% highlight bash %}  
   strings /lib64/libc.so.6 |grep GLIBC_
  {% endhighlight %} 
    
    2. 版本查找
    
     {% highlight bash %}  
   rpm -qa |grep glibc
  {% endhighlight %} 
  
    3. 手工编译
    
    下载地址 <http://www.gnu.org/software/libc/>  
     {% highlight bash %}  
   mkdir build  
   cd build  
   ../configure --prefix=/opt/glibc-2.14
   make -j4
   make install
   {% endhighlight %} 
     4. 导出路径
      {% highlight bash %}  
   export LD_LIBRARY_PATH=/opt/glibc-2.14/lib:$LD_LIBRARY_PATH 
  {% endhighlight %} 
    
    这个有个坑爹的东西，直接加到系统变量里面，结果系统都进不了中文环境了，一直报GUI错什么的，后来只是临时export一下，倒是可以了
 

