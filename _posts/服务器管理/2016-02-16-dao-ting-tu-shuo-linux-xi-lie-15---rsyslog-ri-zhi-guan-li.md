---
layout: single
title: "道听途说Linux系列15 - rsyslog日志管理"
description: "通过rsyslog集中管理Linux日志"
category: "服务器管理"
modified: 2016-02-16 19:55
tags: "linux rsyslog debug"
---
{% include JB/setup %}

传输

接受


调试

*.* /var/log/debugfmt;RSYSLOG_DebugFormat

http://blog.gerhards.net/2013/06/rsyslog-how-can-i-see-which-field.html

Debug line with all properties:
FROMHOST: '10.171.254.94', fromhost-ip: '10.171.254.94', HOSTNAME: '10.171.254.94', PRI: 13,
syslogtag 'nginx-access-wechat^^||{"@timestamp":', programname: 'nginx-access-wechat^^||{"@timestamp"', APP-NAME: 'nginx-access-wechat^^||{"@timestamp"', PROCID: '-', MSGID: '-',
TIMESTAMP: 'Feb 16 19:49:50', STRUCTURED-DATA: '-',
msg: '"2016-02-16T19:46:53+08:00","host":"121.40.144.102","clientip":"58.100.3.154","size":"416","responsetime":"0.009","httpxforwardedfor":"-","timelocal":"16/Feb/2016:19:46:53 +0800","request":"POST /api/index/news/lastest HTTP/1.1","requestbody":"{\x22device\x22:{\x22deviceId\x22:\x228f8a02e27855a189a28ea4babcc6264da333d441\x22,\x22os\x22:2,\x22versionNum\x22:\x221.0.7\x22,\x22netType\x22:\x22WIFI\x22,\x22versionCode\x22:\x221.0.7\x22,\x22ip\x22:\x22192.168.1.100\x22,\x22osVer\x22:\x228.2\x22}}","bodybytessent":"416","upstreamtime":"0.008","upstreamhost":"10.252.91.197:8080","http_host":"wechat.yaomaitong.cn","url":"/api/index/news/lastest","xff":"-","referer":"-","agent":"Medicine/1.0.7 (iPhone; iOS 8.2; Scale/3.00)","contentlength":"168","httpreferer":"-","httpcookie":"-","httpreferer":"-","agent":"Medicine/1.0.7 (iPhone; iOS 8.2; Scale/3.00)","status":"200"}'
escaped msg: '"2016-02-16T19:46:53+08:00","host":"121.40.144.102","clientip":"58.100.3.154","size":"416","responsetime":"0.009","httpxforwardedfor":"-","timelocal":"16/Feb/2016:19:46:53 +0800","request":"POST /api/index/news/lastest HTTP/1.1","requestbody":"{\x22device\x22:{\x22deviceId\x22:\x228f8a02e27855a189a28ea4babcc6264da333d441\x22,\x22os\x22:2,\x22versionNum\x22:\x221.0.7\x22,\x22netType\x22:\x22WIFI\x22,\x22versionCode\x22:\x221.0.7\x22,\x22ip\x22:\x22192.168.1.100\x22,\x22osVer\x22:\x228.2\x22}}","bodybytessent":"416","upstreamtime":"0.008","upstreamhost":"10.252.91.197:8080","http_host":"wechat.yaomaitong.cn","url":"/api/index/news/lastest","xff":"-","referer":"-","agent":"Medicine/1.0.7 (iPhone; iOS 8.2; Scale/3.00)","contentlength":"168","httpreferer":"-","httpcookie":"-","httpreferer":"-","agent":"Medicine/1.0.7 (iPhone; iOS 8.2; Scale/3.00)","status":"200"}'
inputname: imtcp rawmsg: 'nginx-access-wechat^^||{"@timestamp":"2016-02-16T19:46:53+08:00","host":"121.40.144.102","clientip":"58.100.3.154","size":"416","responsetime":"0.009","httpxforwardedfor":"-","timelocal":"16/Feb/2016:19:46:53 +0800","request":"POST /api/index/news/lastest HTTP/1.1","requestbody":"{\x22device\x22:{\x22deviceId\x22:\x228f8a02e27855a189a28ea4babcc6264da333d441\x22,\x22os\x22:2,\x22versionNum\x22:\x221.0.7\x22,\x22netType\x22:\x22WIFI\x22,\x22versionCode\x22:\x221.0.7\x22,\x22ip\x22:\x22192.168.1.100\x22,\x22osVer\x22:\x228.2\x22}}","bodybytessent":"416","upstreamtime":"0.008","upstreamhost":"10.252.91.197:8080","http_host":"wechat.yaomaitong.cn","url":"/api/index/news/lastest","xff":"-","referer":"-","agent":"Medicine/1.0.7 (iPhone; iOS 8.2; Scale/3.00)","contentlength":"168","httpreferer":"-","httpcookie":"-","httpreferer":"-","agent":"Medicine/1.0.7 (iPhone; iOS 8.2; Scale/3.00)","status":"200"}'

过滤

日志格式是一个坑，包含了路径和文件内容，容易弄错
地址也是一个坑，建议的tcp？
调试可以解决一部分问题
rawmsg好像会改变些什么，msg里面确实没有时间，raw里面的内容又太多了，有点奇怪的感觉，后来是通过模板补上的，或者换个词就好了？再看吧

日志分割方法，用脚本，用其他的，等等