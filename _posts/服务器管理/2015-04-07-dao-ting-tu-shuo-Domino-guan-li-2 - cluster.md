---
layout: post
title: "道听途说Domino管理2 - cluster"
description: "domino群集管理配置"
category: "服务器管理"
modified: 2015-04-07 15:04
tags: "Domino管理 Cluster"
---
"test-jb-setup"

## Cluster

   到底叫群集还是集群，是傻傻分不清楚的。
   这个可能是翻译的问题，其实英文单词是一样的。

## 能做什么

   * 为了失效转移方便  
   	当一台服务器宕机的时候，另外一台服务器的数据能接着服务，当然数据也是最新的
   * 为了实现负载均衡   
    实现同一功能的一系列服务器，可以均衡负载

   一般认为，我们关注2个方面的内容：  
   
   * 数据存储
   * 计算能力。
   
   对负载均衡更多的是计算能力的分担。

## 配置
   其实配置是很简单的，   
   
   服务器直接同步。当然指副本
   * 好像也做不了啥
   
   后续更新：
   如何配置，几种应用场景，常见问题
   
   ===