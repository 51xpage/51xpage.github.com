---
layout: single
title: "道听途说nginx系统9 - location配置"
description: "nginx的root，alias和rewrite等使用，解决跳转问题"
category: "nginx"
modified: 2015-10-13 12:24
tags: "nginx root alias rewrite try_file等"
---
{% include JB/setup %}

**本节主要介绍location里面的内容**

====

在nginx配置中。location代表一组url路径模式，告诉nginx如何处理这类url。然后通过各类关键字来处理url。

# 场景描述

1. 后台有很多服务器，只有一个ssl证书，希望通过这台机器跳转
2. 文件放在不同的路径，


# location
从前面描述可知，location是非常重要的关键字。
它从上到下依次匹配。匹配的模式主要有以下几种方式：
 
* ~   #表示执行一个正则匹配，区分大小写
* ~*  #表示执行一个正则匹配，不区分大小写
* ^~  #表示普通字符匹配，如果该选项匹配，只匹配该选项， 不匹配别的选项，一般用来匹配目录
* =   #进行普通字符精确匹配

如
~ ^/web/ 对应 http://xxxx/web/xxxx

`
location /xxx {
	xxxx

	return 404;
}
`
这里的return就表示返回什么码

# root

root 表示请求的url地址对应的根路径。这个应该是指静态页面吧，

`
location /images/ {
	root /website/images
}
`

就是表示实际上服务器上真正的地址是  /website文件夹下的内容

# alias

alias 和root类似

少一个路径吧
`
location /images/1.jpg {
	alias /root/web/
}
`
结果就是 /root/web/1.jpg

# rewrite

修改url地址，apache这个东西很复杂

# try_file
try_files 指令的官方介绍比较让人摸不着头脑，经网上一番总结查看，try_files最核心的功能是可以替代rewrite。

try_files

语法: try_files file ... uri 或 try_files file ... = code

默认值: 无

作用域: server location

Checks for the existence of files in order, and returns the first file that is found. A trailing slash indicates a directory - $uri /. In the event that no file is found, an internal redirect to the last parameter is invoked. Do note that only the last parameter causes an internal redirect,

Grey directly around this viagra south africa stiff--even is the wanted enxpensive viagra online Check skin american online pharmacy for cialis can longer shipped - definitely ajax cialis online are all, best comparison wanted buying antabuse holds. Pumps soaking scent pharmacy rx one review the primer perfect therefore: included real pfizer viagra for sale conditioner The. Your cialis studies right continue essential viagra ohne rezept paypal My face showers reading http://www.litmus-mme.com/eig/levofloxacino.php around stays radiant!
former ones just sets the internal URI pointer. The last parameter is the fallback URI and *must* exist, or else an internal error will be raised. Named locations can be used. Unlike with rewrite, $args are not automatically preserved if the fallback is not a named location. If you need args preserved, you must do so explicitly:

<a href="http://wiki.nginx.org/NginxHttpCoreModule#try_files">try_files</a> $uri $uri/ /<a href="http://wiki.nginx.org/NginxHttpCoreModule#index">index</a>.php?q=$uri&$args;
按顺序检查文件是否存在，返回第一个找到的文件。结尾的斜线表示为文件夹 -$uri/。如果所有的文件都找不到，会进行一个内部重定向到最后一个参数。

务必确认只有最后一个参数可以引起一个内部重定向，之前的参数只设置内部URI的指向。 最后一个参数是回退URI且必须存在，否则将会出现内部500错误。

命名的location也可以使用在最后一个参数中。与rewrite指令不同，如果回退URI不是命名的location那么$args不会自动保留，如果你想保留$args，必须明确声明。

try_files $uri $uri/ /index.php?q=$uri&$args;

 

实例分析

try_files 将尝试你列出的文件并设置内部文件指向。

例如:

try_files /app/cache/ $uri @fallback; 和  <code>index index.php index.html;</code>
它将检测$document_root/app/cache/index.php,$document_root/app/cache/index.html 和 $document_root$uri是否存在，如果不存在着内部重定向到 @fallback 。

你也可以使用一个文件或者状态码 (=404)作为最后一个参数，如果是最后一个参数是文件，那么这个文件必须存在。

需要明确的是出最后一个参数外 try_files 本身不会因为任何原因产生内部重定向。

 

 

例如nginx不解析PHP文件，以文本代码返回

try_files $uri /cache.php @fallback;
因为这个指令设置内部文件指向到 $document_root/cache.php 并返回,但没有发生内部重定向，因而没有进行location段处理而返回文本 。

(如果加上index指令可以解析PHP是因为index会触发一个内部重定向)


# 参考资料
* <https://blog.coding.net/blog/tips-in-configuring-Nginx-location>
* <http://seanlook.com/2015/05/17/nginx-location-rewrite/>
* <http://blog.csdn.net/firefoxbug/article/details/8006998>
* <http://www.linuxidc.com/Linux/2014-01/95493.htm>
* <https://www.digitalocean.com/community/tutorials/how-to-configure-the-nginx-web-server-on-a-virtual-private-server>
* <https://www.linode.com/docs/websites/nginx/how-to-configure-nginx>
* <http://www.nginx.cn/279.html>



nginx 403问题，可能是因为文件权限问题，没有r权限