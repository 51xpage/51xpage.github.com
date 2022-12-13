---
layout: single
title: "道听途说nginx系列5 - ssl配置"
description: "nginx ssl配置"
category: "nginx"
tags: "nginx 网络 反向代理 proxy"
---
{% include JB/setup %}

# 1、背景知识

## 1.1、加密


## 1.2、证书  
# 1、SSL是什么
   SSL(Secure Socket Layer),字面理解就是安全套接字层。针对Socket。作为网络安全的基础，自1994年开发以来，SSL一直发挥着巨大的作用。  
   
## 1.1、为什么需要SSL

### 1.1.1、http传输
   http协议作为web的重要协议，一直因为安全问题为大家所诟病。http的基本模式如下：  
   
   _______
   |      |                     |
   | 用户  |    <=====网络=====> | 服务器  
   |______|                     |
   
   有别于一般私有协议，也因为它的开放性，http传输的是明文。如果在传输路由上截取并篡改内容，影响将是致命的。
   
   对于客户端和服务器双方而已，安全问题包含3个层面：  
   
   * 防篡改
   * 防抵赖
   * 防窥视   防止传输过程内容被  
    
###1.1.2、加密传输
   我们很容易就想到，如果我们不是明文传输，而是加密传输，确实可以有效解决窥视问题。一定程度上也解决了篡改的问题了。但是也会带来几个问题，
  
   * 服务器客户端改造。因为是私有协议，所以需要重新调整
   * 加密方式选择。采用何种加密方式将成为一个很重要的考量
   
为什么需要ssl
加密是怎么回事
ssl解决了什么问题
应该怎么解决

内置根证书

证书都有哪些

# 2、生成自签名SSL

# 3、申请认证SSL

	

# 4、Domino相关

# 5、nginx配置

### 5.1、基本配置

我们知道，https的默认端口是443，所以对应的需要加一个server区段。


server {

	listen               443;
    server_name          xxxx;
    ssl                  on;
    ssl_certificate      server.cer;
    ssl_certificate_key  server.key;
}

这里可以看到有cer文件和key文件，其实我用的是crt文件。

还有很多默认的配置其实省略掉了

强制ssl

证书路径

为什么需要证书
证书里面包含了什么


ssl_ciphers ALL:!ADH:!EXPORT56:-RC4+RSA:+HIGH:+MEDIUM:-EXP;

# 常见问题

* SSL received a record that exceeded the maximum permissible length

	最后发现是ssl on没加
	
