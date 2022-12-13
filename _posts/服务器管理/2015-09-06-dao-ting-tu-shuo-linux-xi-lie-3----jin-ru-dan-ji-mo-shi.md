---
layout: single
title: "道听途说Linux系列3 - 进入单机模式"
description: "忘记密码或者因为配置修改错误无法进入，如何解决"
category: "服务器管理"
modified: 2015-09-06 10:20
tags: "Linux 单机模式 单用户模式 grub"
---
{% include JB/setup %}
# 1、问题描述
### 1.1、密码忘记了无法登陆Linux
  机器就在身边，不想重装。  
### 1.2、配置修改错误，无法进入
  为了解决避免Linux自动休眠，找了文章说修改xorg.conf。结果发现没这个文件，而是一个文件夹。进入修改文件。

vi /etc/X11/xorg.conf

Option      "DPMS" "false"
Section "ServerFlags"  
    Option      "BlankTime" "0"  
    Option      "StandbyTime" "0"  
    Option      "SuspendTime" "0"  
    Option      "OffTime" "0"  
EndSection  
然后就杯具了，进不去了。原因是Option要在某个EndSection下面

# 2、解决方案

### 2.1、进入单用户模式
linux启动的时候有个地方可以选择进入什么模式，这里可以通过操作进入grub。在CentOS7下面没发现 a 操作键，而只有c和e。
c就是进入grub的命令行界面，输入一些命令发现没用。
比如输入 root(hd0)  就没有效果。干脆就进入e。界面有点像是一个脚本文件。通过上下键定位到  
  linux16开头的这一行，找到ro，改成rw init=/sysroot/bin/sh。
  然后用快捷键  ctrl + x重启
  
  再次进入会到命令行界面，但是这个时候通过 ls命令会发现里面内容很少。/etc/下面没有 X11文件夹。所以需要通过命令来切换
  
  {% highlight bash %}  
  chroot /sysroot/
  {% endhighlight %} 
  
  就会发现文件多了很多。 如果需要修改密码可以直接  
  {% highlight bash %} 
  passwd root  
  {% endhighlight %}  
### 2.2、禁止自动休眠

修改 /etc/X11/xorg.conf.d/00-keyboard.conf

Section "InputClass"
        Identifier "system-keyboard"
        MatchIsKeyboard "on"
        Option "XkbLayout" "cn"
EndSection 
  Section "ServerFlags"
        Option "BlankTime" "0"
        Option "StandbyTime" "0"
        Option "SuspendTime" "0"
        Option "OffTime" "0"
EndSection
Section "Monitor"
        Option "DPMS" "false"
EndSection
  
# 3、其他技巧
* 用gedit修改xorg.conf下面的文件时，如果Option的参数是不存在的，系统就会用不同的颜色标识出来，这也算是一个惊喜了吧
* 修改修改grub操作发现还是比较麻烦的，一直失败，以后有机会再折腾吧