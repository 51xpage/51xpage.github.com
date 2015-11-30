---
layout: post
title: "浅滩拾遗 - mysql按天统计信息"
description: "mysql按天统计，按月统计，求和等"
category: "数据库管理"
modified: 2015-11-30 16:16
tags: "mysql group days DATE_FORMAT"
---
{% include JB/setup %}

#1、问题提出

按天统计新增数据，想用一句话搞定

#2、解决方案

{% highlight sql  %} 

select DATE_FORMAT(create_time,'%Y%u') weeks,count(*) count from t_product group by weeks;  

后面的 weeks可以换成 days和months

{% endhighlight %} 