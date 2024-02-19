---
layout: post
title: "道听途说mac系列2 - sublime text"
description: "mac下sublime text使用心得"
category: "瞎折腾"
modified: 2015-04-12 13:33
tags: "sublime-text"
---


## 设置快捷命令
{% highlight bash %}  
  sudo ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/sb
{% endhighlight %}

  快捷键就变成sb了，原来用vim，现在可以直接用sb了。
  另外sb还可以打开当前文件夹下面的所有文件
  {% highlight bash %}  
  sb .
{% endhighlight %}

## 文本选择

多重文本选择：ctrl + cmd + g
列模式选择   option + 左键

Ctrl + T
   找文件中包含内容的地方

Ctrl + D 找相同的字符串

Ctrl + Option + F
    格式化代码

Ctrl + P
Ctrl + R
ctrl + G
Ctrl + H
Ctrl + F(回车, shift回车)
Ctrl + Shift + F

## Pylinter提示lint.py
* remove package pylinter
* 安装 SublimeLinter。