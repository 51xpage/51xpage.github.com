---
layout: single
title: "道听途说nginx系列8 - ganglia集成"
description: "nginx ganglia集成"
category: "nginx"
tags: "nginx 网络 反向代理 proxy"
---
{% include JB/setup %}


inotes打不开首选项，经过测试发现是 login那个，就是没有任何模式匹配的那个地址如果没有自动跳就会有问题，可能是因为跳不到自己服务器上了

ip_hash也需要注意一下，总的那个就不要了，下面的可以要？

yum 不能转本地是因为 路径不对？不能在media里面，要放到mnt等这样的本地路径，靠
