---
layout: post
title: "浅滩拾遗 - AIX下Domino安装记"
description: "AIX下Domino安装碰到的几个问题"
category: "Domino管理"
modified: 2015-05-18 10:19
tags: "Domino AIX ksh bash 乱码"
---
"test-jb-setup"

#1、 问题描述
1. Domino可以安装，但是无法打语言包  
   一直提示不支持的Domino版本 
2. 安装以后无法远程配置  
   提示IO没开什么的
   
2个安装错误提示：

* Your system must be configred with I/O completion Ports
* ServiceException：(error code = 200；message = “iLLegal XML character； &#8； ”；sererity) QJMLException error code=3000   
  
#2、 解决思路
##2.1、 安装错误
* ServiceException其实是因为语言引起的，修改了系统的语言环境就好了。只是需要重启一下。

##2.2、 语言包
#### 2.2.1、路径问题  
  **因为操作失误，导致路径不正确。**  
  AIX默认的shell是ksh，这个shell对退格和删除不是很人性化，在进入安装前创建文件夹，和安装过程中如果有输入信息的地方，一旦输出错误，要调整修改，就会很麻烦。  
   比如安装路径是
   {% highlight bash %}    
    /local1/data.
   {% endhighlight %}  
   其中多了一个 **1**
   结果退格的时候其实删除不全，但是在屏幕上看到是 /local，实际上文件夹名字可能是
   {% highlight bash %}  
   **al**local**  
   {% endhighlight %}  
   类似这样。通过ls命令查看的时候，看起来是正常的，但是在通过FTP客户端查看的时候，就会发现异常。
    
    解决思路：
    1. 通过FlashFXP这样的客户查看文件名，比如在AIX看起来路径是 local，但是在FlashFXP可能是 lxxcal（xx是圆点）。
    然后回到AIX里面，把shell换成bash，通过tab自动补全的方式，删除路径。
    2.在进入安装程序以后，默认还是采用ksh，这个时候，可以采用复制粘贴的方式避免输入错误。事先在记事本之类的地方把东西写好拷贝进去。
    
#### 2.2.2、安装顺序 
  **Domino安装以后直接装语言包失败**  
  原因不详，可能是因为安装用户的权限问题。直接安装是不行。可能换了root就可以了。不过没尝试。
  
  最后的做法是先安装FP2，再安装语言包，然后继续就好了。

###2.3、 配置
* I/O的问题应该是指IOCP服务没开，Domino远程配置的客户端无法连接上，server -listen的时候会提示的

  
# 总结步骤
1. 切换成bash
2. 修改语言环境 smitty lang，改成中文，一般不是UTF-8
3. 启用IOCP， smitty iocp，设置成Available
4. 重启AIX
5. 安装Domino程序
6. 安装FP2
7. 安装语言包
8. 安装其他补丁
9. 配置  

# 一些心得
1. 其实真不是ksh有啥好处的，暂时g没上，也没去查，b去查查不出特别有价值的东西，就老老实实用bash吧，人性化很多
2. smitty简单使用  
   退出 ESC + 0  
   选择下拉框 F4
3. 查看硬盘空间
   {%  highlight bash  %}
    du -sG
   {% endhighlight %}
   
   显示以G为单位的空间情况
4. 删除文件夹
   {%  highlight bash  %}
    rm -R
   {% endhighlight %}

