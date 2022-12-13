---
layout: single
title: "浅滩拾遗 - 磁盘空间无法释放解决一例"
description: "通过lsof查看已经被删除文件占用空间，停止任务释放空间"
category: "服务器管理"
modified: 2016-04-12 20:58
tags: "linux lsof rsyslog"
---
{% include JB/setup %}





大家共用的开发机io不正常，磁盘空间总是被莫名其妙的占满，怀疑是某些东西在不断的生成日志，，想看下具体是那些进程在使用IO，需要安装一个iotop， 使用命令sudo yum install iotop，安装成功，但是运行iotop时提示

No module named iotop.ui
To run an uninstalled copy of iotop,
launch iotop.py in the top directory

开始还以为是没安装好，卸载了重新安装，问题依然存在。
后来仔细分析了提示信息：No mudule name xxx 应该是python的提示信息，由于服务器上默认的python版本2.4太低，我们自己安装了2.6的版本，并且把/usr/bin/python指向了2.6版本的python，而使用yum安装的库在python2.4的路径下，这就导致直接运行iotop时出现模块不存在的信息，之前yum也有同样的问题。
解决方法也很简单，只需要把安装的iotop -\> /usr/bin/iotop第一行的python运行环境由#!/usr/bin/python改为#!/usr/bin/python2.4即可。


ps -L -C rsyslogd -o command,vsize,rss,%mem,size


locate jstack|awk '$0  /jstack$/ {print $0}'| head -1