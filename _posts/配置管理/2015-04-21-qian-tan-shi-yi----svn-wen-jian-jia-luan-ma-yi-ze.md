---
layout: single
title: "浅滩拾遗 - svn文件夹乱码一则"
description: "解决困扰多年的svn乱码小问题"
category: "配置管理"
modified: 2015-04-21 19:42
tags: "svn 配置管理 乱码 字符集"
---
{% include JB/setup %}

起因很简单，2年前使用Visual SVNServer，用Delphi XE提交代码时，文件夹成为乱码了。
在TortoiseSVN中也打不开文件夹了，故事就这样开始了
中文：
    批量签名
乱码：
    ?\197?\250?\193?\191?\199?\169?\195?\251/
==

## 尝试方案
1. windows下老版本SVN。
    怀疑是编码问题，所以想着在WinXP下安装一个老版本的SVN，看看是不是就能解决GB2312的问题了。
    结果好不容易把虚拟机整出来了，问题依旧，打不开。
2.在Linux下改系统字符集
    想着Windows不行，那就用Linux吧，而且还用命令行。
    下载svn也是个麻烦的过程，第一次下载下来是源码。还满怀希望的编译了一下，哐哐哐全是错。
    修改了Lang，Lc_Type啥啥啥的，最后都不行。放弃了

不用用TortoiseSVN还是命令行都不行

## Edge
因为这个事情，开始对Visual SVNServer就点深恶痛绝了，就开始找替代品。
找到了Edge，非常复杂的系统。强大不强大，对我来说，倒是意义不那么特别大。
在网页上可以浏览版本库，很神奇的进去了。所以想着是不是可以删除呢。

## 简单SVN命令

* list
{% highlight bash %}
    svn list https://127.0.0.1/svn/xxxxx
{% endhighlight %}
* rm
{% highlight bash %}
    svn rm https://127.0.0.1/svn/xxx
{% endhighlight %}

## 解决方案
如果直接使用list命令出来的那个路径，是无法删除的，但是既然Edge里面可以看到这个url路径，而且最后证实（在线解码）就是GB2312编码。
所以就使用URL编码后的地址去删除

不错前面的操作会报错，只要加上-m就可以了

{% highlight bash %}
    svn rm https://127.0.0.1/svn/xxx -m “xxx”
{% endhighlight %}

{% highlight bash %}
svn: E205007: Could not use external editor to fetch log message; consider setti
ng the $SVN_EDITOR environment variable or using the --message (-m) or --file (-
F) options
svn: E205007: None of the environment variables SVN_EDITOR, VISUAL or EDITOR are
 set, and no 'editor-cmd' run-time configuration option was found
 {% endhighlight %}