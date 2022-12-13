---
layout: single
title: "浅滩拾遗 - Python问题记录"
description: "Python的几个问题记录"
category: "Python"
modified: 2016-02-16 16:12
tags: "python 问题记录"
---
{% include JB/setup %}

python很好用，尤其是用过easy_install的朋友更是觉得它的便捷，
卸载命令也很简单 easy_install -m package-name
但是面对源码安装的怎么办呢？
 
setup.py 帮助你纪录安装细节方便你卸载
python setup.py install --record log
这时所有的安装细节都写到 log 里了
想要卸载的时候
cat log | xargs rm －rf
就可以干净卸载了

_configtest.c:1:20: 致命错误：Python.h：没有那个文件或目录
numpy
有人说是因为缺python的开发环境
sudo yum install epel-release
$ sudo yum install libffi-devel python-devel python-pip automake autoconf libtool

通过 install python-dev build-essential可以解决

from hashlib import md5


TypeError: Error when calling the metaclass bases
    module.__init__() takes at most 2 arguments (3 given)
    一般是模块名和类名同样了
    
Use cmd_query_iter for statements with multiple queries.
加一个参数