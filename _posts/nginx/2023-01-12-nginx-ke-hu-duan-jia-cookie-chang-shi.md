---
layout: post
title: "nginx客户端加cookie尝试"
description: "nginx升级加cookie尝试"
category: "nginx"
modified: 2023-01-12 19:55
tags: "nginx openresty lua cookie"
---
* content
{:toc}

> 有个tomcat的应用一直报攻击，看起来也确实被攻击了，尝试让nginx做点啥。ssl开通对现在这个系统没啥用，打算尝试用

<!-- more -->
# 01 现状和诉求
2个服务器，从nginx到tomcat，通过反向代理进来的。tomcat在外网没有端口开放，所有攻击也是针对nginx进来的。这个nginx差不多是10年前安装的，一直没有升级过，正好借此机会升级一下。然后想办法在nginx这里做点文章。


# 02 升级nginx
坚持发现版本resty的，很久以前的版本了，
``` bash
resty -V
```

> resty 0.06
nginx version: openresty/1.9.7.4
built by gcc 4.8.2 20140120 (Red Hat 4.8.2-16) (GCC) 
built with OpenSSL 1.0.1e-fips 11 Feb 2013

## 升级resty
## 基本套路
> 先弄下仓库
``` bash
sudo yum install yum-utils -y
sudo yum-config-manager --add-repo https://openresty.org/package/centos/openresty.repo
```

> 然后升级
``` bash
sudo yum install openresty -y
```
出问题了
```
https://rpm.nodesource.com/pub_5.x/el/7/x86_64/repodata/repomd.xml: [Errno 14] curl#35 - "Peer reports incompatible or unsupported protocol version."
```
> curl升级
换个地址，直接尝试也不行
``` bash
curl: (35) Peer reports incompatible or unsupported protocol version
```

重新弄下，好了。
![](../../images/2023-01-12-nginx-ke-hu-duan-jia-cookie-chang-shi/2023-01-14-23-42-56.png)
## 状况调整
以前安装的时候，估计是编译安装的，没有用yum命令，安装的路径也是自己在/opt下搞的。
现在好了，用yum安装，就相当于有俩了，想一下有啥办法可以简单调整呢？

办法已经找到了，可能其实是可以很简单解决的。
以前为了方便，做了几个快捷方式。

``` bash
vim ~/.bash_profile
```
发现果然在里面

``` bash
PATH=$PATH:$HOME/bin

PATH=/opt/openresty/nginx/sbin:$PATH:$HOME/bin
alias ngx="nginx -p /opt/openresty/nginx/ -c /etc/nginx/nginx.conf"
alias ngxt="nginx -p /opt/openresty/nginx/ -c /etc/nginx/nginx.conf -t"
alias ngxr="nginx -p /opt/openresty/nginx/ -c /etc/nginx/nginx.conf -s reload"
alias ngxv="nginx -p /opt/openresty/nginx/ -v"
alias ngxk="nginx -s stop -p /opt/openresty/nginx/ -c /etc/nginx/nginx.conf"

export PATH
```

通过find命令(find / -name "*resty*")找到新安装的resty在/usr/local/openresty，所以修改一下文件

``` bash
PATH=$PATH:$HOME/bin

PATH=/usr/local/openresty/nginx/sbin:$PATH:$HOME/bin
alias ngx="nginx -p /usr/local/openresty/nginx/ -c /etc/nginx/nginx.conf"
alias ngxt="nginx -p /usr/local/openresty/nginx/ -c /etc/nginx/nginx.conf -t"
alias ngxr="nginx -p /usr/local/openresty/nginx/ -c /etc/nginx/nginx.conf -s reload"
alias ngxv="nginx -p /usr/local/openresty/nginx/ -v"
alias ngxk="nginx -s stop -p /usr/local/openresty/nginx/ -c /etc/nginx/nginx.conf"

export PATH
```

![](../../images/2023-01-12-nginx-ke-hu-duan-jia-cookie-chang-shi/2023-01-15-00-11-06.png)
然后先关闭nginx，执行ngxk。ps 坚持一下
![](../../images/2023-01-12-nginx-ke-hu-duan-jia-cookie-chang-shi/2023-01-15-00-13-08.png)再更新命令
``` bash
source ~/.bash_profile
```
![](../../images/2023-01-12-nginx-ke-hu-duan-jia-cookie-chang-shi/2023-01-15-00-14-07.png)发现还有挺多地方要改。

仔细看了下，改的地方也不多。
* listen 443 --> listen 443 ssl
* ssl on 删除

# 03 光升级有啥意思，来点啥


# 04 发现还是有执行脚本的情况
看起来还是不行，现在的提示是

![](../../images/2023-01-12-nginx-ke-hu-duan-jia-cookie-chang-shi/2023-01-15-15-13-14.png)
现在的思路是，能不能限制这个应用运行的用户，不能有curl的权限呢。
目前看起来tomcat有几个安全性没有做，首先做的事建一个

# 06 tomcat 安全性设置
