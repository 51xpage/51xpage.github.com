---
layout: post
title: "浅滩拾遗 - mysql表名大小写问题"
description: "表名大小写问题"
category: "数据库管理"
modified: 2015-11-24 16:50
tags: "mysql 表名大小写"
---
{% include JB/setup %}

网上抄的，正好遇到了，侵删呗

1. Linux下mysql安装完后是默认：区分表名的大小写，不区分列名的大小写；
2. 用root帐号登录后，在/etc/my.cnf中的[mysqld]后添加添加lower_case_table_names=1，重启MYSQL服务，这时已设置成功：不区分表名的大小写；
lower_case_table_names参数详解：
lower_case_table_names=0
其中0：区分大小写，1：不区分大小写

MySQL在Linux下数据库名、表名、列名、别名大小写规则是这样的：

1. 数据库名与表名是严格区分大小写的；
2. 表的别名是严格区分大小写的；
3. 列名与列的别名在所有的情况下均是忽略大小写的；
4. 变量名也是严格区分大小写的；
