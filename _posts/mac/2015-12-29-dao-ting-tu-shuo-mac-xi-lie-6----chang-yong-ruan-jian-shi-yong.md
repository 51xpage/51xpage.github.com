---
layout: post
title: "道听途说mac系列6 - 常用软件使用"
description: "mac常用软件使用"
category: "mac"
modified: 2015-12-29 16:22
tags: "mac beyond compare"
---
{% include JB/setup %}

#1、 Beyond Compare

   从Windows下一路追过来的，用来很久了。发现一个问题。如果要通过ssh比较文件，在bc里面打开的地址是 
   
   profile: root@xxxxx
   
   是这个用户的主目录，无法打开其他文件夹。偶然发现是在路径后面加?就可以了，
   
   profile: root@xxxx?/opt/xxx
   
