---
layout: post
title: "道听途说Linux系列17 - sudo和权限"
description: "通过sudo控制权限"
category: "服务器管理"
modified: 2016-04-12 20:54
tags: "linux sudo sudoers"
---
"test-jb-setup"



http://icedot.blog.51cto.com/61369/477640


sudo: Sorry, you must have a tty to run sudo Error on a Linux and Unix
前面的括号表示用户身份，后面可以放多个命令或者目录


使用不同账户，执行执行脚本时候sudo经常会碰到
sudo: sorry, you must have a tty to run sudo这个情况，其实修改一下sudo的配置就好了
vi /etc/sudoers (最好用visudo命令)
注释掉 Default requiretty 一行
# Default requiretty
意思就是sudo默认需要tty终端。注释掉就可以在后台执行了。
http://chenall.net/post/linux-sudo-config/