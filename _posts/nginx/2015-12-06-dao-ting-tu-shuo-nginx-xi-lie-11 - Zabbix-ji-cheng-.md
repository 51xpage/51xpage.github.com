---
layout: post
title: "道听途说nginx系列11 - Zabbix集成"
description: "nginx开启监控供zabbix使用"
category: "nginx"
modified: 2015-12-06 12:45
tags: "nginx zabbix stub_status"
---
"test-jb-setup"

# 1、问题提出

   想要上一套监控系统，所以研究了一点点ngix对外提供监控的方法，目前了解的情况，nginx对外提供监控的方法是设置一个url地址，里面加一个特殊的参数。

# 2、解决过程
#2.1、 nginx配置


  在location里面顶一个监控需要的地址，如下：  
  
  {% highlight bash %}    
  location /ngx_status {  
  		stub_status on;  
        access_log off;  
        allow 127.0.0.1;  
        allow 10.162.67.111;  
        deny all;  
  }  
  {% endhighlight %}  
  
  这里有3个关键参数：
  
  * stub_status on  
  它表示这个地址匹配的结果是提供统计信息。
  * allow 127.0.0.1等  
  它表示允许访问该服务的地址，多个不知道是用什么分隔的，新行是可以的。
  对于zabbix监控而言，zabbix主机并不会直接访问，而是通过本地进程实现。所以开放给127.0.0.1就可以了
  * deny all;  
  不加这个，前面加了也不会生效，拒绝其他地址连接
  * access_log off;  
  这个不需要开启，直接关闭好了
  

#2.2、 zabbix-agent配置

  本质上，zabbix对nginx的监控是通过zabbix-agent来完成的，所以需要借助zabbix-agent的功能来实现。
  
  * 创建执行文件
 	{% highlight bash %}   
  mkdir /etc/zabbix/scripts
  vim /etc/zabbix/scripts/ngx_status.sh 

  #!/bin/bash    
  # DateTime: 2015-10-25  
  # AUTHOR：凉白开  
  # WEBSITE: http://www.ttlsa.com  
  # Description：zabbix监控nginx性能以及进程状态  
  # Note：此脚本需要配置在被监控端，否则ping检测将会得到不符合预期的结果  
   
  HOST="127.0.0.1"  
  PORT="80"  
   
  # 检测nginx进程是否存在  
  function ping {  
      /sbin/pidof nginx | wc -l   
  }  
  # 检测nginx性能  
  function active {  
      /usr/bin/curl "http://$HOST:$PORT/ngx_status/" 2>/dev/null| grep 'Active' | awk '{print $NF}'  
  }  
  function reading {  
      /usr/bin/curl "http://$HOST:$PORT/ngx_status/" 2>/dev/null| grep 'Reading' | awk '{print $2}'  
  }  
  function writing {  
      /usr/bin/curl "http://$HOST:$PORT/ngx_status/" 2>/dev/null| grep 'Writing' | awk '{print $4}'  
  }  
  function waiting {  
      /usr/bin/curl "http://$HOST:$PORT/ngx_status/" 2>/dev/null| grep 'Waiting' | awk '{print $6}'  
  }  
  function accepts {  
      /usr/bin/curl "http://$HOST:$PORT/ngx_status/" 2>/dev/null| awk NR==3 | awk '{print $1}'  
  }  
  function handled {  
      /usr/bin/curl "http://$HOST:$PORT/ngx_status/" 2>/dev/null| awk NR==3 | awk '{print $2}'  
  }  
  function requests {  
      /usr/bin/curl "http://$HOST:$PORT/ngx_status/" 2>/dev/null| awk NR==3 | awk '{print $3}'  
  }  
  # 执行function  
  $1   
  
  {% endhighlight %}

  * 设置权限
  
  {% highlight bash %}  
  chmod +x /etc/zabbix/scripts/ngx_status.sh   
  {% endhighlight %}

  * 监控设置
  {% highlight bash %} 
  cat << EOF > /etc/zabbix/zabbix_agent.d/userparameter_nginx.conf  
  >UserParameter=nginx.status[*],/etc/zabbix/scripts/ngx_status.sh $1  
  >EOF  
  {% endhighlight %} 
  
  * 重启
  {% highlight bash %}  
  service zabbix-agent restart
  {% endhighlight %} 
  
  * 测试
  通过 zabbix-get
  
# 2.3、zabbix-server配置

导入模板即可

# 3、常见问题
有种可能是ngx_status.sh 没有加执行权限，可以通过 /var/zabbix/zabbix_agent.log查看

# 4、参考资料

<http://www.ttlsa.com>