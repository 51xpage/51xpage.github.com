---
layout: post
title: "浅滩拾遗 - mysql通过select更新记录"
description: "mysql通过select更新记录"
category: "数据库管理"
modified: 2015-11-24 16:29
tags: "mysql"
---
"test-jb-setup"

# 问题提出

系统通过select查到另外一个表的数据，然后根据id更新到当前表中，减肥查询，oracle，mssql和mysql方法差别很大，下面是mysql的方式

# 问题解决
{% highlight sql %}
UPDATE t_store INNER JOIN `tuser`  ON tstore.tel=y_user.`mobilephone` 
SET `tstore`.`user_id` =`tuser`.`id` 
{% endhighlight %}