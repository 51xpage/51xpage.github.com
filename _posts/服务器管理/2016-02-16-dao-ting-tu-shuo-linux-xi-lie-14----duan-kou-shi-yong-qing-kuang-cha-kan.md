---
layout: post
title: "道听途说Linux系列14 - 端口使用情况查看"
description: "Linux下查看端口使用情况"
category: "服务器管理"
modified: 2016-02-16 14:42
tags: "linux netstat ss 端口"
---
{% include JB/setup %}

ss -tnl
查看监听地址

netstat -lntp

以后把几个工具结合起来写吧，还有iftop等等