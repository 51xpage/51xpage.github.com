---
layout: single
title: "浅滩拾遗 - Delphi开发Activex记录"
description: "Delphi控件开发问题记录"
category: "桌面开发"
modified: 2016-11-10 10:35
tags: "Office Delphi ActiveX Cookie Indy ssh"
---
{% include JB/setup %}


一打开就crash，看起来好像是因为type xxx那个改了一下就坏了

加了一个ssh的控件，然后就一直报错，怎么弄怎么报错，整的我胆战心惊的，先做减法，把加的东西都去了，把main里面的内容都去了
改了一下以后发现，还是一直报错，

版本恢复，好了。慢慢加回去，发现是tlb文件的问题，用XE5改了一下就好了

另外发现下载上传一直不行，后来才发现是因为FS对象把文件给占住了，

400的问题，一直提示这个，最开始找了很多资料，网上提示说是indy版本的问题，10.0之类的版本会有bug，

https://svn.atozed.com:444/svn/Indy10/tags/Indy%2010.6.2%20-%20Seattle%20Upd1/Lib/
用户名是Indy_Public_RO。

改indy代码
IdHttp.pas
搜索
Delphi/Pascal code
?
1
ARequest.URL := URL.GetPathAndParams;

改成
Delphi/Pascal code
?
1
ARequest.URL := URL.Path + URL.Document + URL.Params;

最后发现，问题其实很简单，本来代码都不需要动，就是文件名要转义一下，就可以了，靠

最后发现另外一个服务器是好的，用同样的cookie就是好的，所以比较奇怪，最后抓包发现其实是根本没发起http的请求，发现请求是乱码
可能还是控件的什么属性问题，先不管了，

用idcookiemanager是不行了

====

一直有问题，2013，链接不了事件，后来发现提示错误是 interface not supported。不知道啥原因

用d7 和 xe 5看看

一开始想着是什么原因，后来发现那里不报错了，把变量改出来，单独赋值，但是用exl看还是那里错，一直怀疑是后面的问题，后来才发现其实是因为
传入的变量根本就是空值，

现在看看为什么是空值，比较奇怪的时候，前面看不是空值。getlasterror返回时127，说明dll加载失败了，都会有哪些dll呢

====

add_header Set-Cookie "LtpaToken=${cookie_LtpaToken};Domain=.huclife.com;Path=/;Max-Age=21111111";

nginx后来是通过另外写cookie搞定的，不知道行不行

##add_header "Access-Control-Allow-origin" "http://*.huclife.com";
##add_header "Access-Control-Allow-Methods" "GET, POST, OPTIONS";








========

控件一开始就死一开始就死，结果发现是因为获取MainForm的initialization函数有问题，nnd，想多了

=======

控件奇怪了，升级的时候会出现冲突的问题，原来是cab安装的，是delphi7做的，后来用delphi xe 做了以后，升级就吹冲突
但是如果这个时候改成不同的名字的ocx，就又没问题了，但是老的也不能用了
