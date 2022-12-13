---
layout: single
title: "道听途说Jenkins系统3 - 常用插件"
description: "插件安装方式，几种常用插件"
category: "配置管理"
modified: 2015-10-06 21:07
tags: "jenkins git scm maven"
---
{% include JB/setup %}

	默认情况下，Jenkins已经安装了很多插件，可以从服务器管理界面看到


#1、安装方式
* 在线安装  
	Jenkins通过系统管理的Web界面可以直接安装插件，另外还会提示需要更新的插件，使用非常方便。
* 离线安装  
	由于网络等原因，有些插件无法通过在线方式安装，可以通过离线的方式安装。还是在在线安装的位置，有一个高级标签，里面可以上传插件并安装。
	
	通常安装失败会有提示信息，告知可能是网络超时等等，我们可以根据这个url去下载插件文件（扩展名是hpi）

这里的搜索过滤功能还不错。
另外官方还有一个专门的地址可以下载插件。<https://wiki.jenkins-ci.org/display/JENKINS/Plugins>

# 2、常用插件  

### 2.1 git

  默认情况下，jenkins目前不支持git，而是需要通过插件来完成。git比较特别需要2个插件，git和git-client，非常幸运的是，这俩插件在线安装失败了，然后就通过上面的离线方式解决了，在官网可以下载到，反正需要俩一起装，好像是先装git。
  
	GIT plugin/GIT client plugin

### 2.2 maven

  因为项目是基于maven的。所以需要这个插件，装好以后会发现，新建项目的时候，有一个maven的项目类型，这也算是一个扩展了。
  
	Maven Integration plugin
  
### 2.3 ssh
   这个插件的作用，可以说是调用远程的命令执行，完成一些工作

	Publish Over SSH
	
### 2.4 scm
   其实还不知道它是干嘛的，先拷贝一段话吧
   
   尽管Git库可以同步多个git库，但是需要注意的是Git插件提供branch选项尽管可是该多个，但是是针对与每一个库同时检索多个branch，这个不符合我们使用的原则。对于部署来说，只需要调用一个Git库中的一个分支。
   
   <http://blog.csdn.net/disappearedgod/article/details/43406019>
   	
	Multiple SCMs plugin

### 2.5 邮件通知
   邮件通知折腾了好长时间，主要是目的是让通知的形式更丰富一点，内容可以扩展一点

	Email Extension Plugin/Email Extension Template Plugin