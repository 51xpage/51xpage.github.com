---
layout: post
title: "道听途说Jenkins系统6 - git配置"
description: "如何设置从git获取代码并执行"
category: "配置管理"
modified: 2015-10-06 21:10
tags: "jenkins git"
---
{% include JB/setup %}

参考资料 <https://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin>

#1、全局配置
全局配置比较简单，在git区段
主要是git的命令路径，默认使用git。
也就是说，我们通过客户端登陆上来以后，git能使用就不用管理，通常是可以的。也可以指定一个详细的路径。

如果没有安装也可以让jenkins来安装，我没去折腾，原来就装好了

#2、项目配置
安装了git插件以后，在项目的源码那里会有一个git的选项。指定git的地址。后台采用gogs，它会告诉我们ssh和http地址。

有2种方式登陆。


### 2.1 web方式
它指定一个url地址，gogs默认是3000端口，如

http://xxxx:3000/xxxxx.git

另外需要配置一个用户名，它使用的是jenkins本身的一个Credentials。它指定不同的认证认识。这里采用 用户名/密码

### 2.2 ssh方式

还是上面的地方，使用ssh key的方式。

不管用上面方式，它都会马上告诉我们是否成功。但是我发现ssh方式很杯具的失败了，等我搞定了再完善这个文章吧

#3、调试
发现用ssh失败了以后，系统给出一个命令

Failed to connect to repository : Command "git -c core.askpass=true ls-remote -h git@127.0.0.1:xxx/api.git HEAD" returned status code 128:
stdout: 

所以我理解应该在jenkins这个服务器上可以访问git才对。而我已经在gogs上把key放进去了，为啥还是不行呢。如果我在jenkins服务器上通过命令行可以访问应该就没有了吧。

所以开了2个终端，一个执行  
{% highlight bash %}    
ssh -v host -l user  
{% endhighlight %}
从这个命令可以看到连接进来的人，以及验证的情况。

另外一个执行 

{% highlight bash %}    
ssh -vvv -T git@服务器
{% endhighlight %}

这个上一篇文章介绍过，可以看到整个执行过程，不过然并卵，没搞定

{% highlight bash %} 
debug1: Found key in /root/.ssh/known_hosts:4
debug1: ssh_ecdsa_verify: signature correct
debug2: kex_derive_keys
debug2: set_newkeys: mode 1
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug2: set_newkeys: mode 0
debug1: SSH2_MSG_NEWKEYS received
debug1: Roaming not allowed by server
debug1: SSH2_MSG_SERVICE_REQUEST sent
debug2: service_accept: ssh-userauth
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug2: key: /root/.ssh/id_rsa_jenkins (0x7f293cff9af0), explicit
debug1: Authentications that can continue: publickey,gssapi-keyex,gssapi-with-mic,password
debug3: start over, passed a different list publickey,gssapi-keyex,gssapi-with-mic,password
debug3: preferred publickey
debug3: authmethod_lookup publickey
debug3: remaining preferred: 
debug3: authmethod_is_enabled publickey
debug1: Next authentication method: publickey
debug1: Offering RSA public key: /root/.ssh/id_rsa_jenkins
debug3: send_pubkey_test
debug2: we sent a publickey packet, wait for reply
debug1: Authentications that can continue: publickey,gssapi-keyex,gssapi-with-mic,password
debug2: we did not send a packet, disable method
debug1: No more authentication methods to try.
Permission denied (publickey,gssapi-keyex,gssapi-with-mic,password).
{% endhighlight %}

或者用这个来测试连接情况
{% highlight bash %} 
ssh -p 1022 -i ~/.ssh/id_rsa_jenkins -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null git@test.com
{% endhighlight %}