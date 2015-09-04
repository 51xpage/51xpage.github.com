---
layout: post
title: "道听途说Linux系统1 - tewmviewer安装"
description: "centos下安装Teamviewer记录"
category: "服务器管理"
modified: 2015-09-04 15:47
tags: "teamviewer linux rpm yum centos"
---
{% include JB/setup %}
# 1. 问题描述
 直接安装的时候，用rpm命令，提示错误。  
 {% highlight bash %}  
 	rpm -ivh teamviewer.i686.rpm  
{% endhighlight %}   

警告：teamviewer.i686.rpm: 头V4 DSA/SHA1 Signature, 密钥 ID 72db573c: NOKEY  
错误：依赖检测失败：  
	libc.so.6(GLIBC_2.4) 被 teamviewer-10.0.46203-0.i686 需要  
	libgcc_s.so.1 被 teamviewer-10.0.46203-0.i686 需要  
	libasound.so.2 被 teamviewer-10.0.46203-0.i686 需要  
	libfontconfig.so.1 被 teamviewer-10.0.46203-0.i686 需要  
	libfreetype.so.6 被 teamviewer-10.0.46203-0.i686 需要  
	libjpeg.so.62 被 teamviewer-10.0.46203-0.i686 需要  
	libpng12.so.0 被 teamviewer-10.0.46203-0.i686 需要  
	libSM.so.6 被 teamviewer-10.0.46203-0.i686 需要  
	libXdamage.so.1 被 teamviewer-10.0.46203-0.i686 需要  
	libXext.so.6 被 teamviewer-10.0.46203-0.i686 需要  
	libXfixes.so.3 被 teamviewer-10.0.46203-0.i686 需要  
	libXinerama.so.1 被 teamviewer-10.0.46203-0.i686 需要  
	libXrandr.so.2 被 teamviewer-10.0.46203-0.i686 需要  
	libXrender.so.1 被 teamviewer-10.0.46203-0.i686 需要  
	libXtst.so.6 被 teamviewer-10.0.46203-0.i686 需要  
	libz.so.1 被 teamviewer-10.0.46203-0.i686 需要  

# 2、解决办法
### 2.1、安装本地源，就是光盘源  
  这个比较简单，直接在 yum.repo.d下面拷贝一个文件     
  然后修改成本地路径名，注意一下空格的转义就可以了  
{% highlight bash %}      
  yum clean all  
  yum update    
{% endhighlight %}     
### 2.2、用yum安装
{% highlight bash %}    
yum localinstall teamviewer.i686.rpm  
{% endhighlight %}    
已加载插件：fastestmirror, langpacks
正在检查 teamviewer.i686.rpm: teamviewer-10.0.46203-0.i686  
teamviewer.i686.rpm 将被安装    
正在解决依赖关系  
--> 正在检查事务  
---> 软件包 teamviewer.i686.0.10.0.46203-0 将被 安装  
--> 正在处理依赖关系 libc.so.6(GLIBC_2.4)，它被软件包 teamviewer-10.0.46203-0.i686 需要  
Loading mirror speeds from cached hostfile  
 * base: mirrors.163.com  
 * extras: mirrors.skyshe.cn  
 * updates: mirrors.163.com  
--> 正在处理依赖关系 libgcc_s.so.1，它被软件包 teamviewer-10.0.46203-0.i686 需要  
--> 正在处理依赖关系 libasound.so.2，它被软件包 teamviewer-10.0.46203-0.i686 需要  
--> 正在处理依赖关系 libfontconfig.so.1，它被软件包 teamviewer-10.0.46203-0.i686 需要  
--> 正在处理依赖关系 libfreetype.so.6，它被软件包 teamviewer-10.0.46203-0.i686 需要  
--> 正在处理依赖关系 libjpeg.so.62，它被软件包 teamviewer-10.0.46203-0.i686 需要  
--> 正在处理依赖关系 libpng12.so.0，它被软件包 teamviewer-10.0.46203-0.i686 需要  
--> 正在处理依赖关系 libSM.so.6，它被软件包 teamviewer-10.0.46203-0.i686 需要  
--> 正在处理依赖关系 libXdamage.so.1，它被软件包 teamviewer-10.0.46203-0.i686 需要  
--> 正在处理依赖关系 libXext.so.6，它被软件包 teamviewer-10.0.46203-0.i686 需要  
--> 正在处理依赖关系 libXfixes.so.3，它被软件包 teamviewer-10.0.46203-0.i686 需要  
--> 正在处理依赖关系 libXinerama.so.1，它被软件包 teamviewer-10.0.46203-0.i686 需要  
--> 正在处理依赖关系 libXrandr.so.2，它被软件包 teamviewer-10.0.46203-0.i686 需要  
--> 正在处理依赖关系 libXrender.so.1，它被软件包 teamviewer-10.0.46203-0.i686 需要  
--> 正在处理依赖关系 libXtst.so.6，它被软件包 teamviewer-10.0.46203-0.i686 需要  
--> 正在处理依赖关系 libz.so.1，它被软件包 teamviewer-10.0.46203-0.i686 需要  
--> 正在检查事务  
---> 软件包 alsa-lib.i686.0.1.0.28-2.el7 将被 安装  
---> 软件包 fontconfig.i686.0.2.10.95-7.el7 将被 安装  
--> 正在处理依赖关系 libexpat.so.1，它被软件包 fontconfig-2.10.95-7.el7.i686 需要  
---> 软件包 freetype.i686.0.2.4.11-10.el7_1.1 将被 安装  
---> 软件包 glibc.i686.0.2.17-78.el7 将被 安装  
--> 正在处理依赖关系 libfreebl3.so(NSSRAWHASH_3.12.3)，它被软件包 glibc-2.17-78.el7.i686 需要  
--> 正在处理依赖关系 libfreebl3.so，它被软件包 glibc-2.17-78.el7.i686 需要  
---> 软件包 libSM.i686.0.1.2.1-7.el7 将被 安装  
--> 正在处理依赖关系 libuuid.so.1(UUID_1.0)，它被软件包 libSM-1.2.1-7.el7.i686 需要  
--> 正在处理依赖关系 libuuid.so.1，它被软件包 libSM-1.2.1-7.el7.i686 需要  
--> 正在处理依赖关系 libICE.so.6，它被软件包 libSM-1.2.1-7.el7.i686 需要  
---> 软件包 libXdamage.i686.0.1.1.4-4.1.el7 将被 安装  
--> 正在处理依赖关系 libX11.so.6，它被软件包 libXdamage-1.1.4-4.1.el7.i686 需要  
---> 软件包 libXext.i686.0.1.3.2-2.1.el7 将被 安装  
---> 软件包 libXfixes.i686.0.5.0.1-2.1.el7 将被 安装  
---> 软件包 libXinerama.i686.0.1.1.3-2.1.el7 将被 安装  
---> 软件包 libXrandr.i686.0.1.4.1-2.1.el7 将被 安装  
---> 软件包 libXrender.i686.0.0.9.8-2.1.el7 将被 安装  
---> 软件包 libXtst.i686.0.1.2.2-2.1.el7 将被 安装  
--> 正在处理依赖关系 libXi.so.6，它被软件包 libXtst-1.2.2-2.1.el7.i686 需要  
---> 软件包 libgcc.i686.0.4.8.3-9.el7 将被 安装  
---> 软件包 libjpeg-turbo.i686.0.1.2.90-5.el7 将被 安装  
---> 软件包 libpng12.i686.0.1.2.50-6.el7 将被 安装  
---> 软件包 zlib.i686.0.1.2.7-13.el7 将被 安装  
--> 正在检查事务  
---> 软件包 expat.i686.0.2.1.0-8.el7 将被 安装  
---> 软件包 libICE.i686.0.1.0.8-7.el7 将被 安装  
---> 软件包 libX11.i686.0.1.6.0-2.1.el7 将被 安装  
--> 正在处理依赖关系 libxcb.so.1，它被软件包 libX11-1.6.0-2.1.el7.i686 需要  
---> 软件包 libXi.i686.0.1.7.2-2.1.el7 将被 安装  
---> 软件包 libuuid.i686.0.2.23.2-22.el7_1.1 将被 安装  
---> 软件包 nss-softokn-freebl.i686.0.3.16.2.3-13.el7_1 将被 安装  
--> 正在检查事务  
---> 软件包 libxcb.i686.0.1.9-5.el7 将被 安装  
--> 正在处理依赖关系 libXau.so.6，它被软件包 libxcb-1.9-5.el7.i686 需要  
--> 正在检查事务  
---> 软件包 libXau.i686.0.1.0.8-2.1.el7 将被 安装  
--> 解决依赖关系完成    

依赖关系解决

============================================================================================================================================================================================================
 Package                                              架构                                   版本                                                  源                                                  大小
============================================================================================================================================================================================================
正在安装:
 teamviewer                              /25               i686                                   10.0.46203-0                                          /teamviewer.i686                                   122 M
为依赖而安装:
 alsa-lib                                             i686                                   1.0.28-2.el7                                          base                                               391 k
 expat                                                i686                                   2.1.0-8.el7                                           base                                                80 k
 fontconfig                                           i686                                   2.10.95-7.el7                                         base                                               229 k
 freetype                                             i686                                   2.4.11-10.el7_1.1                                     updates                                            388 k
 glibc                                                i686                                   2.17-78.el7                                           base                                               4.2 M
 libICE                                               i686                                   1.0.8-7.el7                                           base                                                62 k
 libSM                                                i686                                   1.2.1-7.el7                                           base                                                37 k
 libX11                                               i686                                   1.6.0-2.1.el7                                         base                                               608 k
 libXau                                               i686                                   1.0.8-2.1.el7                                         base                                                29 k
 libXdamage                                           i686                                   1.1.4-4.1.el7                                         base                                                20 k
 libXext                                              i686                                   1.3.2-2.1.el7                                         base                                                38 k
 libXfixes                                            i686                                   5.0.1-2.1.el7                                         base                                                18 k
 libXi                                                i686                                   1.7.2-2.1.el7                                         base                                                39 k
 libXinerama                                          i686                                   1.1.3-2.1.el7                                         base                                                14 k
 libXrandr                                            i686                                   1.4.1-2.1.el7                                         base                                                25 k
 libXrender                                           i686                                   0.9.8-2.1.el7                                         base                                                25 k
 libXtst                                              i686                                   1.2.2-2.1.el7                                         base                                                20 k
 libgcc                                               i686                                   4.8.3-9.el7                                           base                                                99 k
 libjpeg-turbo                                        i686                                   1.2.90-5.el7                                          base                                               137 k
 libpng12                                             i686                                   1.2.50-6.el7                                          base                                               181 k
 libuuid                                              i686                                   2.23.2-22.el7_1.1                                     updates                                             74 k
 libxcb                                               i686                                   1.9-5.el7                                             base                                               178 k
 nss-softokn-freebl                                   i686                                   3.16.2.3-13.el7_1                                     updates                                            187 k
 zlib                                                 i686                                   1.2.7-13.el7                                          base                                                90 k

事务概要
============================================================================================================================================================================================================
安装  1 软件包 (+24 依赖软件包)

总计：129 M
总下载量：7.1 M
安装大小：143 M
Is this ok [y/d/N]: y
Downloading packages:
(1/24): expat-2.1.0-8.el7.i686.rpm                                                                                                                                                   |  80 kB  00:00:00    
(2/24): libICE-1.0.8-7.el7.i686.rpm                                                                                                                                                  |  62 k  B  00:00:00  
(3/24): libSM-1.2.1-7.el7.i686.rpm                                                                                                                                                   |  37 kB  00:00:00  
(4/24): libX11-1.6.0-2.1.el7.i686.rpm                                                                                                                                                | 608 kB  00:00:00  
(5/24): libXau-1.0.8-2.1.el7.i686.rpm                                                                                                                                                |  29 kB  00:00:00  
(6/24): libXdamage-1.1.4-4.1.el7.i686.rpm                                                                                                                                            |  20 kB  00:00:00  
(7/24): libXext-1.3.2-2.1.el7.i686.rpm                                                                                                                                               |  38 kB  00:00:00  
(8/24): libXfixes-5.0.1-2.1.el7.i686.rpm                                                                                                                                             |  18 kB  00:00:00  
(9/24): libXi-1.7.2-2.1.el7.i686.rpm                                                                                                                                                 |  39 kB  00:00:00  
(10/24): libXinerama-1.1.3-2.1.el7.i686.rpm                                                                                                                                          |  14 kB  00:00:00  
(11/24): libXrandr-1.4.1-2.1.el7.i686.rpm                                                                                                                                            |  25 kB  00:00:00  
(12/24): alsa-lib-1.0.28-2.el7.i686.rpm                                                                                                                                              | 391 kB  00:00:02
(13/24): libXrender-0.9.8-2.1.el7.i686.rpm                                                                                                                                           |  25 kB  00:00:00  
(14/24): libXtst-1.2.2-2.1.el7.i686.rpm                                                                                                                                              |  20 kB  00:00:00  
(15/24): libgcc-4.8.3-9.el7.i686.rpm                                                                                                                                                 |  99 kB  00:00:00  
(16/24): libjpeg-turbo-1.2.90-5.el7.i686.rpm                                                                                                                                         | 137 kB  00:00:00  
(17/24): fontconfig-2.10.95-7.el7.i686.rpm                                                                                                                                           | 229 kB  00:00:03
(18/24): libpng12-1.2.50-6.el7.i686.rpm                                                                                                                                              | 181 kB  00:00:00  
(19/24): freetype-2.4.11-10.el7_1.1.i686.rpm                                                                                                                                         | 388 kB  00:00:03
(20/24): libuuid-2.23.2-22.el7_1.1.i686.rpm                                                                                                                                          |  74 kB  00:00:00  
(21/24): zlib-1.2.7-13.el7.i686.rpm                                                                                                                                                  |  90 kB  00:00:00  
(22/24): nss-softokn-freebl-3.16.2.3-13.el7_1.i686.rpm                                                                                                                               | 187 kB  00:00:00  
(23/24): libxcb-1.9-5.el7.i686.rpm                                                                                                                                                   | 178 kB  00:00:01
(24/24): glibc-2.17-78.el7.i686.rpm                                                                                                                                                  | 4.2 MB  00:00:06
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
总计                                                                                                                                                                        1.0 MB/s | 7.1 MB  00:00:06
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  正在安装    : libgcc-4.8.3-9.el7.i686                                                                                                                                                                1/25  
  正在安装    : glibc-2.17-78.el7.i686                                                                                                                                                                 2/25  
  正在安装    : nss-softokn-freebl-3.16.2.3-13.el7_1.i686                                                                                                                                              3/25  
  正在安装    : freetype-2.4.11-10.el7_1.1.i686                                                                                                                                                        4/25  
  正在安装    : zlib-1.2.7-13.el7.i686                                                                                                                                                                 5/25  
  正在安装    : expat-2.1.0-8.el7.i686                                                                                                                                                                 6/25  
  正在安装    : fontconfig-2.10.95-7.el7.i686                                                                                                                                                          7/25  
  正在安装    : libpng12-1.2.50-6.el7.i686                                                                                                                                                             8/25  
  正在安装    : libICE-1.0.8-7.el7.i686                                                                                                                                                                9/25  
  正在安装    : libjpeg-turbo-1.2.90-5.el7.i686                                                                                                                                                       10/25  
  正在安装    : libXau-1.0.8-2.1.el7.i686                                                                                                                                                             11/25  
  正在安装    : libxcb-1.9-5.el7.i686                                                                                                                                                                 12/25  
  正在安装    : libX11-1.6.0-2.1.el7.i686                                                                                                                                                             13/25  
  正在安装    : libXext-1.3.2-2.1.el7.i686                                                                                                                                                            14/25  
  正在安装    : libXfixes-5.0.1-2.1.el7.i686                                                                                                                                                          15/25  
  正在安装    : libXrender-0.9.8-2.1.el7.i686                                                                                                                                                         16/25  
  正在安装    : libXrandr-1.4.1-2.1.el7.i686                                                                                                                                                          17/25  
  正在安装    : libXdamage-1.1.4-4.1.el7.i686                                                                                                                                                         18/25  
  正在安装    : libXinerama-1.1.3-2.1.el7.i686                                                                                                                                                        19/25  
  正在安装    : libXi-1.7.2-2.1.el7.i686                                                                                                                                                              20/25  
  正在安装    : libXtst-1.2.2-2.1.el7.i686                                                                                                                                                            21/25  
  正在安装    : libuuid-2.23.2-22.el7_1.1.i686                                                                                                                                                        22/25  
  正在安装    : libSM-1.2.1-7.el7.i686                                                                                                                                                                23/25  
  正在安装    : alsa-lib-1.0.28-2.el7.i686                                                                                                                                                            24/25  
  正在安装    : teamviewer-10.0.46203-0.i686                                                                                                                                                          25/25  
  验证中      : libICE-1.0.8-7.el7.i686                                                                                                                                                                1/25  
  验证中      : fontconfig-2.10.95-7.el7.i686                                                                                                                                                          2/25  
  验证中      : freetype-2.4.11-10.el7_1.1.i686                                                                                                                                                        3/25  
  验证中      : teamviewer-10.0.46203-0.i686                                                                                                                                                           4/25  
  验证中      : libXext-1.3.2-2.1.el7.i686                                                                                                                                                             5/25  
  验证中      : libXdamage-1.1.4-4.1.el7.i686                                                                                                                                                          6/25  
  验证中      : nss-softokn-freebl-3.16.2.3-13.el7_1.i686                                                                                                                                              7/25  
  验证中      : libXinerama-1.1.3-2.1.el7.i686                                                                                                                                                         8/25  
  验证中      : libjpeg-turbo-1.2.90-5.el7.i686                                                                                                                                                        9/25  
  验证中      : libgcc-4.8.3-9.el7.i686                                                                                                                                                               10/25  
  验证中      : libXau-1.0.8-2.1.el7.i686                                                                                                                                                             11/25  
  验证中      : libSM-1.2.1-7.el7.i686                                                                                                                                                                12/25  
  验证中      : libXrandr-1.4.1-2.1.el7.i686                                                                                                                                                          13/25  
  验证中      : libpng12-1.2.50-6.el7.i686                                                                                                                                                            14/25  
  验证中      : libXtst-1.2.2-2.1.el7.i686                                                                                                                                                            15/25  
  验证中      : libXfixes-5.0.1-2.1.el7.i686                                                                                                                                                          16/25  
  验证中      : libX11-1.6.0-2.1.el7.i686                                                                                                                                                             17/25  
  验证中      : libuuid-2.23.2-22.el7_1.1.i686                                                                                                                                                        18/25  
  验证中      : libXi-1.7.2-2.1.el7.i686                                                                                                                                                              19/25  
  验证中      : zlib-1.2.7-13.el7.i686                                                                                                                                                                20/25  
  验证中      : alsa-lib-1.0.28-2.el7.i686                                                                                                                                                            21/25  
  验证中      : libxcb-1.9-5.el7.i686                                                                                                                                                                 22/25  
  验证中      : libXrender-0.9.8-2.1.el7.i686                                                                                                                                                         23/25  
  验证中      : expat-2.1.0-8.el7.i686                                                                                                                                                                24/25  
  验证中      : glibc-2.17-78.el7.i686                                                                                                                                                                25/25  

已安装:
  teamviewer.i686 0:10.0.46203-0

作为依赖被安装:
  alsa-lib.i686 0:1.0.28-2.el7          expat.i686 0:2.1.0-8.el7            fontconfig.i686 0:2.10.95-7.el7                  freetype.i686 0:2.4.11-10.el7_1.1      glibc.i686 0:2.17-78.el7
  libICE.i686 0:1.0.8-7.el7             libSM.i686 0:1.2.1-7.el7            libX11.i686 0:1.6.0-2.1.el7                      libXau.i686 0:1.0.8-2.1.el7            libXdamage.i686 0:1.1.4-4.1.el7
  libXext.i686 0:1.3.2-2.1.el7          libXfixes.i686 0:5.0.1-2.1.el7      libXi.i686 0:1.7.2-2.1.el7                       libXinerama.i686 0:1.1.3-2.1.el7       libXrandr.i686 0:1.4.1-2.1.el7
  libXrender.i686 0:0.9.8-2.1.el7       libXtst.i686 0:1.2.2-2.1.el7        libgcc.i686 0:4.8.3-9.el7                        libjpeg-turbo.i686 0:1.2.90-5.el7      libpng12.i686 0:1.2.50-6.el7
  libuuid.i686 0:2.23.2-22.el7_1.1      libxcb.i686 0:1.9-5.el7             nss-softokn-freebl.i686 0:3.16.2.3-13.el7_1      zlib.i686 0:1.2.7-13.el7

完毕！