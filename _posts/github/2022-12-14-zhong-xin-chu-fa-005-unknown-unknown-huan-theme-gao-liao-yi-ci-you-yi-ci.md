---
layout: post
title: "重新出发005——换theme搞了一次又一次"
description: "jekyll的theme是咋回事，好复杂"
category: "github"
modified: 2022-12-14 08:52
tags: "jekyll github pages"

---
* content
{:toc}

## 1 主题和皮肤什么鬼
theme和skin，深究下来会更复杂一些。只是个人理解，有失偏颇在所难免。
theme比skin更大一些，可以理解为，theme包括了布局，不光光皮肤，类似背景颜色等等。
如果是这样的理解方式，我们就会知道，theme实际上，包含
* layout，用来处理布局
* css,js,image，用来处理颜色等
* include, 公用内容

大致可以理解，jekyll的原理就是通过 layout去集成css和js，生成一个静态页面。
其中的css，js 和image一般来说，是公用的，目录引用正确就可以了。

## 2 弯路1，想得太玄乎
发现有命令来换皮肤，但是没有前面的理解，以为是很玄乎的内容。
想着就图快，赶快搞定。
``` bash
rake theme:install 
rake theme:switch
```
类似这样的命令，本质上应该就是换了上面的那些东西。
>后来发现是因为有个Rakefile文件，里面有这些代码。尴尬




## 3 在线安装hacker
比较喜欢这个皮肤，就打算尝试一下
``` bash
rake theme:install git="https://github.com/pages-themes/hacker.git"

Cloning into './_theme_packages/_tmp'...
remote: Enumerating objects: 444, done.
remote: Total 444 (delta 0), reused 0 (delta 0), pack-reused 444
Receiving objects: 100% (444/444), 105.06 KiB | 703.00 KiB/s, done.
Resolving deltas: 100% (208/208), done.
rake aborted!
Errno::ENOENT: No such file or directory @ rb_sysopen - ./_theme_packages/_tmp/manifest.yml
```
比较遗憾，出错了，手工建个文件夹呗，可以弄下来了。

>但是有个发现，用这个命令的很多demo网址，更新时间都在2010年前后，也是很多年前的事了。
对ruby不熟悉，也就不深究了，姑且认为是jekyllbootstrap这个体系下的东西都比较老吧。

## 4 发现Gemfile文件
以前没有这个问题，说明jekyll升级了，我的博客比较老，那我能不能建一个呢？
手工建立了一个可以。

弄好了执行bundle命令
```
bundle
Fetching gem metadata from https://rubygems.org/...........
Resolving dependencies........
Using bundler 2.3.26
Using concurrent-ruby 1.1.10
Using colorator 1.1.0
Fetching commonmarker 0.23.6
Fetching execjs 2.8.1
Fetching minitest 5.16.3
Fetching thread_safe 0.3.6
Fetching public_suffix 4.0.7
Fetching unf_ext 0.0.8.2
Fetching zeitwerk 2.6.6
Fetching coffee-script-source 1.11.1
Installing zeitwerk 2.6.6
Using eventmachine 1.2.7
Using http_parser.rb 0.8.0
```

## 5 弯路2，layout中的包含

折腾一圈下来好像没啥用，本地看起来，少css，
无意中发现 _layout文件夹里面的文件有点问题。


``` yaml
---
layout: default
---
{- % include JB/setup % }
{-  % include themes/hsptr/_config.yml % }
```

类似这样的，于是把它改成hacker看看
基本上都改了一遍。大致算完成了
但是hacker上去以后和我想象中还是有差距，导航条啥的，还需要自己折腾一下，无意中发现minimal Mistakes听不错的

## 6 Minimal Mistakes
基于上面的理解，这回直接把仓库弄下来，把几个文件夹内容换掉，核心保留_posts里面的内容就可以了。

比较遗憾的是，一直没有成功（hacker以后，github的action里面一直有失败），界面可能也是比较适合英文的。

## 7 换主题643435675.github.io

同意的做法，这次弄下来以后，才发现github的action可能是我以前设置的，也可能是系统自带的，rerun了以后发现问题所在，就改好了

## 8 主题网址
* http://jekyllthemes.org/  这个网址里面有很多主题，但是都有点简单
* https://github.com/jekyll/jekyll/wiki/Sites 这里就能找到比较多样式了
另外知乎上也有专题


