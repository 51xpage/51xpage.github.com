---
layout: post
title: "浅滩拾遗 - mysql通过字符串函数更新"
description: "mysql中使用字符串函数，获取另外字段内容，组合以后更新记录"
category: "数据库管理"
modified: 2015-11-24 16:41
tags: "mysql"
---
"test-jb-setup"
# 问题提出

希望将用户手机号最后4位加一个固定的字符串，生成用户的昵称

# 解决方案

{% highlight sql %}
update `tuser` set `nickname` =  CONCAT("会员" , substr(`mobilephone`, 8,4))  where nickname is null or `nickname` like '会员%'

{% endhighlight %}
