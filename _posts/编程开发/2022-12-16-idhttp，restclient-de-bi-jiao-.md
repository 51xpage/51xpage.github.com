---
layout: post
title: "idhttp，restclient的比较"
description: "jekyll的theme是咋回事，好复杂"
category: "编程开发"
modified: 2022-12-16 00:09
tags: "idhttp restclient unigui Delphi"
---
* content
{:toc}

# Delphi下的http请求

以前的学习工作经历，用得比较多的是idhttp，也用习惯了。最近发现它不能很好处理http异常。所以找了一些其他的办法。
这里说的不能很好处理是指，http返回的不是200，而是400之类的，在默认情况下，idhttp认为是正常的，但是我们的业务逻辑上已经出问题了。
说白了，不管是什么语言，都还是要遵循http规范。
都不过是一个普通的http客户端而已，至于是用chrome，还是我们自己写的代码。
想清楚这点，很容易就明白了。我们不过是发个请求，处理个响应而已。

# idhttp
这个以前是第三方的，后来应该是纳入产品了。从D7开始一直用这个东西，也算是熟门熟路了。

### 基础使用

``` Delphi
uses idhttp;

TIdHTTP.Create;


```

### get和post

### 带上cookie
很多服务器都是通过cookie来验证。
回到根本上来说，我们就是要组装一个结构，发给服务器。
这个结构有header，也有body。

``` Delphi
uses idhttp;

IdHTTP1.CustomHeader;

IdHTTP1.RawHeader;


```

### https


# restclient
因为idhttp的状况，打算

### 基础使用

# 工具


# 总结一些
* 用restclient还有个好处，在unigui里面，fiddle可以捕获，idhttp好像不行
* idhttp如果连https，需要dll文件