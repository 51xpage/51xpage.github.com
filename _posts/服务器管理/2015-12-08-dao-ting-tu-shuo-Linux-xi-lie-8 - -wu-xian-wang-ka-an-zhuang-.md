---
layout: post
title: "道听途说Linux系列8 - 无线网卡安装"
description: "Linux下无线网卡安装"
category: "服务器管理"
modified: 2015-12-08 23:30
tags: "linux wireless 无线网卡 TP-Link"
---
"test-jb-setup"

买了一个TP-Link ，还有点贵的
安装里面没有linux驱动，官网倒是有，结果装不上，编译的时候各种报错

后来别人说这个是Realteck的什么鬼，估计是内核

lsusb。可以看到一些东西，

然后有些人就说这个东西，里面有个型号，估计是注册到use什么什么鬼的东西吧，也没装上.编译各种错


https://sites.google.com/site/easylinuxtipsproject/reserve-7#TOC-Realtek-RTL8192EU-chipset-0bda:818b-

http://blog.163.com/thinki_cao/blog/static/83944875201311481635188

http://askubuntu.com/questions/346919/does-anyone-have-drivers-for-a-tp-link-tl-wn823n-usb-wireless

http://www.linux-hardware-guide.com/zh/2013-04-21-tp-link-tl-wn823n-mini-wireless-n-usb-300mbps

http://ubuntuforums.org/showthread.php?t=2266703

https://wikidevi.com/wiki/TP-LINK_TL-WN823N_v1


于是，换了一个东西。

https://drive.google.com/file/d/0B_PyshAvItmPX3pwVEhKNEdDRTA/view

用这个东西可以装了。也可以搜索信号了，但是最后报错了


Bus 001 Device 006: ID 0bda:8178 Realtek Semiconductor Corp. RTL8192CU 802.11n WLAN Adapter


iwlist

iwconfig

http://lyjilu.iteye.com/blog/2059084

https://sites.google.com/site/easylinuxtipsproject/reserve-7

https://forum.ubuntu.org.cn/viewtopic.php?f=116&t=468417

https://wireless.wiki.kernel.org/en/users/Drivers


想不到echo命令功能这么强大， 能发邮件，还能下载东西什么的


