---
layout: post
title: "道听途说Jenkins系统11 - 优化建议"
description: "优化建议"
category: "配置管理"
modified: 2015-10-06 21:18
tags: "jenkins 优化建议"
---
"test-jb-setup"

# 1、关闭自动关联编译
   默认情况下好像会自动关联编译，在maven的高级选项里面，有Enable triggering of downstream projects。
   
   把复选框去掉，直接保存无效，需要先应用再保存才可以，比较坑爹