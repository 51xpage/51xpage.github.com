---
layout: post
title: "道听途说Office开发系列1 - 如何通过句柄获取Word对象"
description: "Delphi下获取Word句柄的几种方式"
category: "Office"
modified: 2015-06-03 13:31
tags: "Office VBA COM Delphi ActiveX"
---
{% include JB/setup %}

# 前言
断断续续做了很多年的OA，伴随整个OA生涯的是Office的研发，算是一个回忆吧。

通常Office控件分2种。  

* 嵌入  
   嵌入方式比较好理解，就是在ActiveX控件里面显示Word内容。  
   VC的版本，在微软早起有一个dso的源码。给大家很多思路。
   Delphi版本一般是直接使用OLEContainer控件。
   
   不管用哪种方式，开发成本都是不低的。如果是Delphi的版本，基本也需要自己重写这个对象了。
   国内2个比较有代表性的商业产品正好是2个不同的思路。
    
* 独立
   独立的意思是单独启动Office进程，然后进行交互。首当其冲的问题是如何获取Office对象，并进而让ActiveX和这个对象建立联系。
   
   2种方式都经历过，用得比较多的还是第2种方式。
   
   如果能获取到IDispath接口，就可以和Delphi自己的WordApplication建立关联，也就能捕获Office的事件。

# 如何获取Word对象


## 1、通过com对象
   通过Javascript把word对象传入到ActiveX控件中。
    {% highlight delphi %} 
   unit uCoGetServerPID;


## 2、通过窗口标题
{% highlight delphi %} 
procedure TMainForm.Button3Click(Sender: TObject);

function TMainForm.GetWordHandle(AFileName, AClassName, AFlagText: Widestring)


另外一个封装的东西

{% highlight delphi %} 
