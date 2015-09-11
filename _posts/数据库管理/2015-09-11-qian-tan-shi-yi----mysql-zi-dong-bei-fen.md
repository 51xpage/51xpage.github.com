---
layout: post
title: "浅滩拾忆 - mysql自动备份"
description: "mysql在linux自动备份"
category: "数据库管理"
modified: 2015-09-11 18:17
tags: "mysql mysqldump 备份"
---
{% include JB/setup %}
#1、准备工作
 考虑到通过scp远程备份，所以需要把本地的key传到远程服务器上。
### 1.1、生成key

{% highlight bash %} 
	ssh-keygen -t rsa
{% endhighlight%}

一路回车即可。会在/root/.ssh文件夹下生成2个文件id_rsa，id_rsa.pub


### 1.2、传到远程服务器
将其中的pub文件传到远程服务器的相同文件夹下，改名为
authorized_keys

{% highlight bash %} 
scp /root/.ssh/id_rsa.pub xxxx@xxxxxx:/home/.ssh/authorized_keys
{% endhighlight%} 

#2、备份mysql
	
参考 [mysql 数据库自动备份]: <http://www.xuchanggang.cn/archives/640.html>

###2.1、建立备份脚本

{% highlight bash %} 
#vim backup.sh
#!/bin/bash  
  
# 进入mysqldump命令目录  
  
# 设置备份的时间，备份信息存放文件，备份路径，压缩路径，备份的用户，密码，主机，端口，数据库  
DD=`date +%y-%m-%d==%H:%M:%S`  
LOGFILE=/var/lib/mysql/mysqlbackup.log  
backup_dir=/var/lib/mysql/dbbackup/  
zip_dir=/var/lib/mysql/zipdir/  
dbusername=mysql  
dbpassword=mysql   
host=127.0.0.1  
port=3306   
database1=alldb  
  
# 指定生成备份的文件名，压缩后的文件名  
DumpFile="$database1"$(date +%y%m%d).dump  
NewFile="$database1"$(date +%y%m%d).tgz  
  
# 查看备份的目录是否存在，不存在建立，并修改为mysql权限，并将相应输出信息写入日志文件  
echo "check directory..." >> $LOGFILE  
if [ ! -d $backup_dir ] ;then  
  mkdir -p $backup_dir  
  chown mysql:mysql $backup_dir  
fi  
echo $DD " backup start..." >> $LOGFILE  
echo $DD >>$LOGFILE  
echo "backup "$database1" ..." >> $LOGFILE  
  
# 备份数据库，
# --all-databases表示所有数据库 
# 否则用 --databases db1 db2
mysqldump -h$host -P$port -u$dbusername -p$dbpassword --all-databases > $backup_dir$DumpFile  
 
  
# 进入数据备份目录，压缩备份的文件，压缩完后删除dump文件  
cd $backup_dir  
tar czvf $NewFile $DumpFile >> $LOGFILE 2>&1  
rm -rf $DumpFile  
  
# 判断压缩存放目录是否存在，不存在，建立，修改权限，并将压缩过的备份文件移送到压缩目录  
echo "moving zipfiles ..." >> $LOGFILE  
cd $backup_dir  
if [ ! -d $zip_dir ] ;then  
  mkdir -p $zip_dir  
  chown mysql:mysql $zip_dir  
fi  
 mv *.tgz  $zip_dir  
  
# 备份到远程服务器 
echo "copy to remote server" >> $LOGFILE  
scp $zip_dir$NewFile root@xxxx:/home/backup/
echo "scp complete.." >> $LOGFILE  

#remove before 7 days  
echo "remove before 7 days..." >> $LOGFILE  
find $zip_dir -type f -mtime +7 -exec rm -f {} \;  
echo "backup over" >> $LOGFILE 
{% endhighlight%} 

###2.2、建立定时任务
{% highlight bash %} 
crontab -e
{% endhighlight%} 
添加下面这行
0 3 * * * ./tmp/backup.sh