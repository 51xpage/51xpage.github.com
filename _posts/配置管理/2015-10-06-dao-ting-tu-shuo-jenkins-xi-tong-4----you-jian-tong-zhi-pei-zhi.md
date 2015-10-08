---
layout: post
title: "道听途说Jenkins系统4 - 邮件通知配置"
description: "jenkins邮件通知和通知模板"
category: "配置管理"
modified: 2015-10-06 21:08
tags: "jenkins 邮件通知 通知模板"
---
{% include JB/setup %}

# 1、基本配置
有了这么强大的工具，万一编译失败了咋整。所以通知变得非常重要。Jenkins默认提供了邮件通知的功能。

	jenkins的配置有全局和项目之分。很多配置会体现

### 1.1、smtp配置
在系统管理——>系统配置，可以看到有一个邮件的配置，这里用来配置smtp。整个jenkins都是通过这个来发送邮件的。和一般的客户端（如Foxmail）配置类似。我用的腾讯企业邮箱。所以几个关键配置项如下：

* smtp服务器： smtp.exmail.qq.com
* 用户默认邮件后缀：空。   
这个后缀我猜是简化配置的，比如发送给多个人，只要写名字，不用写@后面的部分
* 勾选使用Smtp验证
* 用户名密码设置好
* 勾选使用SSL
* 端口号是 465
	这个在官网可以查到

最后测试，这里需要输入一个收件人。这个可以随便写。最后提示
	
 		
	Email was successfully sent
表示成功了

### 1.2、常见错误
如果提示

	com.sun.mail.smtp.SMTPSendFailedException: 501 mail from address must be same as authorization user

那恭喜中奖了，其实很简单。在这个页面的 Jenkins Location部分，有一个系统管理员邮件地址，这里要和上面设置的用户名一直，即验证的一致

### 1.3、收件人设置

收件人是在项目中设置的，设置具体项目属性的时候，有一个地方设置收件人以及触发条件。
这里有个需要注意，收件人是通过** 逗号 **分隔的。

# 2、扩展配置
用上面的方法配置出来的邮件比较简单。

* 格式比较简单，
* 只有文本方式
* 触发条件比较单一

所以建议这些原因，增加了2个扩展，上一节已经提到。设置的地方还是在系统管理里面。在**Extended E-mail Notification**区段

### 2.1、基本设置
和上面的配置一样，设置smtp的信息，网上看到有一个配置项，是用来覆盖系统默认的邮件发送设置的。**Override Global Settings**。 但是一直没找到。结果是，如果这里不设置smtp，那就没有自定义的邮件发送，设置了就会收到2封邮件。这不坑爹吗？


### 2.2、内容模板
使用这个配置可以扩展2个部分，邮件的内容格式，已经触发条件。可以设置全局一个模板，具体项目里面直接引用即可(默认值不动)。另外在项目里面设置。里面有2个设置。一个是系统默认的那个邮件设置。里面可以写收件人。

	就是说，系统默认的邮件发送可以设置收件人,但是ext设置了Project Recipient List，并没有卵用


设置的位置比较怪异，是在 **“操作后构建-Enabled Email Notification”**


内容默认需要设置3个内容
* Content Type

text/html

* Default Subject

{% highlight html %}  
构建通知:$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS!
{% endhighlight %}  

* Default Context

{% highlight html %} 
(本邮件是程序自动下发的，请勿回复，<span style="color:red">请相关人员fix it,重新提交到git 构建</span>)<br/>
<hr/>

项目名称：$PROJECT_NAME<br/>
<hr/>

构建编号：$BUILD_NUMBER<br/>
<hr/>


GIT版本号：${GIT_REVISION}<br/>
<hr/>

构建状态：$BUILD_STATUS<br/>
<hr/>

触发原因：${CAUSE}<br/>
<hr/>

构建日志地址：<a href="${BUILD_URL}console">${BUILD_URL}console</a><br/>
<hr/>

构建地址：<a href="$BUILD_URL">$BUILD_URL</a><br/>
<hr/>

变更集:${JELLY_SCRIPT,template="html"}<br/>
<hr/>
{% endhighlight %}  

设置了它以后，还需要设置trigger，不够都没有卵用，反正收件人还是1个人

参考<http://www.juvenxu.com/2011/05/18/hudson-email-ext/>