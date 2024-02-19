---
layout: post
title: "道听途说Linux系列9 - 发送外部邮件"
description: "Linux下发送外部邮件的方法"
category: "服务器管理"
modified: 2015-12-10 22:02
tags: "linux mail echo mailx"
---
"test-jb-setup"

# 1、问题提出

希望通过脚本发送邮件，起因是zabbix里面有个地方需要发邮件。而它在Web上提供的方式比较简单，smtp服务器和helo啥啥啥的，在现在安全连接的时代，显然是不够的，可配置的项很少。好在它提供了另外一种方式，即采用脚本发送的方式。

# 2、尝试过程

根据以往Domino的经验，通常是一来就把sendmail干掉了，发送邮件不能随便一个服务器，马上就被当垃圾邮件被拒信了，而且就算弄个MX记录也麻烦，整个黑名单啥的。所以比较靠谱的方式，还是利用现有的服务器来发，注册一个免费邮箱。

# 2.1、停止 sendmail 和postfix

{% highlight bash %}  
service sendmail stop  
chkconfig sendmail off  
service postfix stop  
chkconfig postfix off  
{% endhighlight %}

# 2.2、使用mail/mailx发送邮件

通过  
{% highlight bash %}  
rpm -qa|grep mailx  
{% endhighlight %}  
命令可以看到系统是否安装了mail。不过发现mail和mailx在centos 7下面是一样的

见识了一下 echo命令，这大概就是Linux系列的强大之处吧，用echo就发邮件了。
{% highlight bash %}  
echo -e "Email content" | mailx -v -s "Email subject" -S smtp-auth=login -S smtp=smtp.163.com -S from="username@gmail.com(John Doe)" -S smtp-auth-user=test@163.com -S smtp-auth-password=passw0rd recipient@some.com  
{% endhighlight %}  

# 2.3、使用mail.rc

用上面的命令行确实可行，但是配置有点乱，所以还有个解决方案是把配置放到 mail.rc里面去
{% highlight bash %}  
# vim /etc/mail.rc
set from=test@163.com   
set smtp=smtp.163.com    
set smtp-auth-user=test   
set smtp-auth-password=password  
set smtp-auth=login  
{% endhighlight %}  

发送邮件的时候，使用
{% highlight bash %}   
echo  "内容" | mail -s " 标题" sendto@163.com  
{% endhighlight %}  

如果碰到需要多个smtp账号就无法处理了，其实它还有另外一种做法。

{% highlight bash %}  
accout 163 {
	set from=test@163.com   
	set smtp=smtp.163.com    
	set smtp-auth-user=test   
	set smtp-auth-password=password  
	set smtp-auth=login  
}
{% endhighlight %}  

相应的，发送命令也需要做调整，如下  
{% highlight bash %}   
echo  "内容" | mail -A 163  -s " 标题" sendto@163.com  
{% endhighlight %}    
即，这里多了一个 -A 参数

# 2.4、发送smtps邮件

用上面的方法无法实现发送带安全验证的邮件。找到参考资料的里面的老外的做法。

{% highlight bash %}   
account exmail {
        set ssl-verify=ignore
        set nss-config-dir=~/.cert
        set from=jenkins@yaomaitong.cn
        set smtp=smtps://smtp.exmail.qq.com:465
        set smtp-auth-user=username@qymail.com
		set smtp-auth-password=s0m3p@zzW0rD
        set smtp-auth=login
}

{% endhighlight %}  

类似这样的，但是会报错，


{% highlight bash %}   

#echo  "内容" | mail -A exmail -v  -s " 标题" sendto@163.com  

Resolving host smtp.exmail.qq.com . . . done.  
Connecting to 163.177.72.143:465 . . . connected.  
Error initializing NSS: Unknown error -8015.  
"/root/dead.letter" 11/300  
. . . message not sent.   
{% endhighlight %}  

可以理解成是没有证书文件，老外的做法是获取生成证书文件。


* 生成证书  
{% highlight bash %}  
mkdir ~/.certs && certutil -N -d ~/.certs  
{% endhighlight %}  

	这个时候会发现，下面生成了几个key和cert文件

* 获取qq邮箱证书  
{% highlight bash %}  
echo -n | openssl s_client -connect smtp.exmail.qq.com:465 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > ~/.certs/exmail.crt  

certutil -A -n "GeoTrust SSL CA" -t "C,," -d ~/.certs -i ~/.certs/exmail.crt

这里的 GeoTrust SSL CA，是打开 https://exmail.qq.com，然后点开看， exmail.qq.com 上一级证书的名字，实际测试发现，其实根本也没关系

{% endhighlight %}  

* 发送测试
{% highlight bash %}  

#echo  "内容" | mail -A exmail -v  -s " 标题" sendto@163.com  
 
Resolving host smtp.exmail.qq.com . . . done.
Connecting to 163.177.72.143:465 . . . connected.
Error in certificate: Peer's certificate issuer is not recognized.
Comparing DNS name: "mx3.qq.com"
Comparing DNS name: "mx2.qq.com"
Comparing DNS name: "mx1.qq.com"
Comparing DNS name: "mxbiz1.qq.com"
Comparing DNS name: "mxbiz2.qq.com"
Comparing DNS name: "imap.qq.com"
Comparing DNS name: "smtp.qq.com"
Comparing DNS name: "pop.exmail.qq.com"
Comparing DNS name: "imap.exmail.qq.com"
Comparing DNS name: "smtp.exmail.qq.com"
SSL parameters: cipher=RC4, keysize=128, secretkeysize=128,
issuer=CN=GeoTrust SSL CA - G2,O=GeoTrust Inc.,C=US
subject=CN=pop.qq.com,OU=R&D,O=Shenzhen Tencent Computer Systems Company Limited,L=Shenzhen,ST=Guangdong,C=CN
220 smtp.qq.com Esmtp QQ Mail Server
>>> EHLO iZ23458bi3lZ
250-smtp.qq.com
250-PIPELINING
250-SIZE 73400320
250-AUTH LOGIN PLAIN
250-AUTH=LOGIN
250-MAILCOMPRESS
250 8BITMIME
>>> AUTH LOGIN
334 xxxxxxx
>>> xxxxxxx
334 xxxxxxx
>>> xxxxxxx==
235 Authentication successful
>>> MAIL FROM:<51xpages@ymtest.cn>
250 Ok
>>> RCPT TO:<51xpages@ymtest.cn>
250 Ok
>>> DATA
354 End data with <CR><LF>.<CR><LF>
>>> .
250 Ok: queued as 
>>> QUIT
221 Bye
{% endhighlight %}   

# 3、最终方案

其实应该来讲，用上面的方法就可以了。但是当时没有配置成功，所以采用了另外的办法。
找到一个装了 firefox的电脑，把~/.mozilla/firefox/xxxxxxxx.default/ 的 cert*.db 与 key*.db 拷贝到 ~/.certs文件夹下。效果居然是一样的。

# 4、几个问题

因为是给zabbix用的，是一个单独的nologin账户，但是测试的时候，是在root用户下做的，通了，但是zabbix无法发邮件，后来发现问题出在 certs路径上，它指向的是当前用户的 .certs文件夹。
然后拷贝过来，发现另外一个问题，权限不对，zabbix没有 r权限，都是root用户的

Error in certificate: Peer's certificate issuer is not recognized.

不加v参数会有这个问题

Error in certificate: Peer's certificate issuer is not recognized.

# 5、参考资料

* 采用sendmail，基本不考虑 <http://yyzll.blog.51cto.com/4283444/1541890>
* 外国人的 <https://coderwall.com/p/ez1x2w/send-mail-like-a-boss>
* 发非smtps哟就<http://coolnull.com/2614.html>
* <http://blog.sina.com.cn/s/blog_56ae1d5801019hlr.html>

参数说明

{% highlight bash%}  
-r 指定发件人
-c 指定抄送人
-b 指定密送人
-s 邮件主题
-V 显示版本
-v 发送过程
多个收件人之间用逗号分隔

{% endhighlight %}  