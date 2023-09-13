---
layout: post
title: "道听途说时间管理系统1 - google日历开发初探"
description: "把上周的完成情况导出到excel中去"
category: "个人成长"
modified: 2015-06-01 21:36
tags: "google 时间管理 日历导出"
---
* content
{:toc}

# 1、背景介绍 
   年初因为看了一些时间管理的书，决定开始管理自己的时间。
   主要是2本影响比较大，
   
   * 介绍柳比歇夫一生的《奇特的一生》
   * 胜间和代的《时间投资法》。这本书淘宝上买也是打印版本，托人去日本也没找到。
   
   沿着这些时间给自己制定了时间管理的方案。
   
   * 每周计划。  
      按工作生活等分类，不同颜色标记。如果完成了就标绿。
   * 时刻记录时间。名字自己的时间消耗情况。  
      它的结果是，发现原来自己对日常生活中的时间估算是不太准的。
      
   定每周一为一周总结时间，把上一周的完成情况做总结。列倒excel中去。  
   经过一段时间的使用，发现从google日历导出成了一个很麻烦的事情。于是想着自动化解决。   
   最直接的方法当然是用google的API来做。于是
   
   
# 2、尝试路径
   相关资料比较多，如果要使用它的api，要注册个应用就行了，教程很多，不再赘述。
   
   本质上这些API都是Rest，所以语言不应该成为障碍。而且在Google的网站上可以测试这些API，大大提高学习效率。
   
   总的来说，2个API：
   
   * 获取日历列表
   * 获取每个日历里面的事件，特别是颜色  
     因为绿色表示已完成，不管是什么日历
     
## 2.1、Python   
   本来想着功能比较简单，也想用python练习一下。就挑了python。结果发现每次都要去跳转到网页，再去处理。语法也确实不熟悉，折腾了很长时间就放弃了。
   
## 2.2、.Net/Delphi
   想着用Python比较麻烦，自己又只是简单用一下，能导出来就行了，所以就想着用.Net，应该比Java方便点吧。   
   结果就照着文档折腾了一把环境，它需要通过NuGet来做，结果就杯具了，这个东西居然被墙，要经过一大堆才能配置好环境。如果不用它自己直接下载那些包，使用也不方便。  
   Delphi需要解决验证问题
   
## 2.3、Java
   咋办勒，算了，那就java吧，真的非常不喜欢这东西，依赖关系比较多。用Java是需要GRADLE。于是照着文档搞了搞，最后把自己搞死了。
   
## 2.4、Javascript
   最后发现它可以，有点太没挑战了吧，好吧，就先这样吧。
   于是照着官方的文档（google+）写了个代码， 然后坑爹的事情出现了。通过API无法获取事件的颜色。只能获取日历的颜色。 
       
# 3、目前方案
经过一段时间的坑爹以后，现在的做法是：

* chrome插件  
   负责通过js读取dom对象，把绿色的事件找出来。
* html页面
   用来接受chrome插件的内容
   请求google api，获取日历事件   
   
## 3.1、chrome插件要点
 基本构成是 
 
 * mainifest.json：用来总体定义
 * 19X19和 38 X 38的png图标：用来显示图标
 * popup.html:默认弹出层
 * content_scripts：表示页面里面要执行的javascript
 
``` json 
 {
	"manifest_version": 2,
	"name": "Google日历导出",
	"version": "0.0.1",
	"background": { "scripts": ["jquery-2.0.0.min.js", "background.js"] },
	"browser_action": {  // 如果是page_action就表示在地址栏里面，否则就是在浏览器按钮那里。
		"default_icon": {
			"19": "google_calendar_19.png",
			"38": "google_calendar_38.png"
		},
		"default_title": "Google日历导出", // shown in tooltip
		"default_popup": "popup.html"
	},
	"permissions" : ["activeTab","tabs"],
	"content_scripts": [ {
          "js":["jquery-2.0.0.min.js", "content_script.js"],
          "matches": [ "http://*/*", "https://*/*" ]
       } ]
}
```
 
大致执行顺序如下：

1. 先执行background的js。它可以用来接受消息。
   **好像不能调试**
2. 执行content_scripts里面的js。
   这个比较特殊，用它来和页面交互，访问页面对象。这个js可以调试。
3. 当点击时弹出popup.html。它里面的js可以执行和conetnt_scripts的交互。**不能调试**。

总的来讲，可以认为popup是对外协调的，由content_scripts访问DOM，然后发送给backgroud来处理。它们之间通过消息来通信。
发送：  
``` javascript 
	chrome.runtime.sendMessage
```
	
接受：
``` javascript 
    chrome.runtime.onMessage.addListener(function(request, sender, sendRequest){
	var beginDate = request.beginDate.split(' ')[0];
	

    if(request.type!=="google-calendar-data")
		return;
	window.open('http://localhost:8000/quickstart.html?beginDate=' + beginDate + '&dateEvents=' + request.dateEvents+ '&' + new Date());
});
```

为了避免加载就执行，所以content_scripts里面可以放函数。

然后在popup的js里面调用。  
``` javascript 
chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.tabs.executeScript(tabs[0].id, {code: "getOKEvents();"});
});
```
 
## 3.2、html页面要点 
``` javascript 
var beginDate, endDate, dateEvents;

// Your Client ID can be retrieved from your project in the Google
// Developer Console, https://console.developers.google.com
var CLIENT_ID = ''

var SCOPES = ['https://www.googleapis.com/auth/calendar'];



/**
 * Check if current user has authorized this application.
 */
function checkAuth() {
  gapi.auth.authorize(
    {
      'client_id': CLIENT_ID,
      'scope': SCOPES,
      'immediate': true
    }, handleAuthResult);
}

/**
 * Handle response from authorization server.
 *
 * @param {Object} authResult Authorization result.
 */
function handleAuthResult(authResult) {
  var authorizeDiv = document.getElementById('authorize-div');
  if (authResult && !authResult.error) {
    // Hide auth UI, then load Calendar client library.
    authorizeDiv.style.display = 'none';
    loadCalendarApi();
  } else {
    // Show auth UI, allowing the user to initiate authorization by
    // clicking authorize button.
    authorizeDiv.style.display = 'inline';
  }
}

/**
 * Initiate auth flow in response to user clicking authorize button.
 *
 * @param {Event} event Button click event.
 */
function handleAuthClick(event) {
  gapi.auth.authorize(
    {client_id: CLIENT_ID, scope: SCOPES, immediate: false},
    handleAuthResult);
  return false;
}

function getURLInfo(){
  var ret = parseURL(location.href);
  beginDate = decodeURIComponent(ret.params['beginDate']);
  beginDate = beginDate.replace(('年'), '-').replace(('月'), '-').replace(('日'),'') + ' 00:00:00';
  beginDate = new Date(beginDate);

  var WeekFirstDay = new Date(beginDate - ( beginDate.getDay()) * 86400000);
  var WeekLastDay = new Date((WeekFirstDay / 1000 + (7) * 86400) * 1000);
  beginDate = WeekFirstDay.toISOString(); //(new Date()).toISOString(),
  endDate= WeekLastDay.toISOString();

  dateEvents = decodeURIComponent(ret.params['dateEvents']);
  return false;
}

/**
 * Load Google Calendar client library. List upcoming events
 * once client library is loaded.
 */
function loadCalendarApi() {
  getURLInfo();
  gapi.client.load('calendar', 'v3', listUpcomingEvents);
}

function buildTable(){
  var tbOutput = [];
  var rowsEvent = 0;
  var rowsCal = 0;
  tbOutput[tbOutput.length] = '<table>';
  for(var obj in lsResult){
    rowsCal = 0;
    tbOutput[tbOutput.length] = '<tr><td rowspan="" style="background:#dcf1db">' + obj + '</td>';
    for(var cal in lsResult[obj]){
      var calObj = lsResult[obj][cal];
      if(cal=='天气')continue;
      if(cal=='農曆')continue;
      rowsEvent = 0;
      tbOutput[tbOutput.length] = '<tr><td rowspan="" style="background:' + calObj.color + '">' + calObj.name + '</td>';
      rowsCal++;
      for(var event in calObj.events){
          rowsEvent++;
          rowsCal++;
          tbOutput[tbOutput.length] = '';
          if(1 < rowsEvent)tbOutput[tbOutput.length - 1] = '<tr>';
          tbOutput[tbOutput.length-1] += '<td style="background:' + calObj.color + '">' + calObj.events[event] + '</td></tr>';
      }
      tbOutput[tbOutput.length - rowsEvent - 1] = tbOutput[tbOutput.length - rowsEvent - 1].replace('rowspan=""', 'rowspan="' + rowsEvent + '"');
    }
    tbOutput[tbOutput.length - rowsCal -1] = tbOutput[tbOutput.length - rowsCal - 1].replace('rowspan=""', 'rowspan="' + (rowsCal -4) + '"').replace("</tr>", "");
    tbOutput[tbOutput.length - rowsCal ] = tbOutput[tbOutput.length - rowsCal ].replace("<tr>", "");
  }
  tbOutput[tbOutput.length] = '</table>';
  $('#tbOutput').html(tbOutput.join(''));
}

/**
 * Print the summary and start datetime/date of the next ten events in
 * the authorized user's calendar. If no events are found an
 * appropriate message is printed.
 */
function listUpcomingEvents() {
  var requestCalendar = gapi.client.calendar.calendarList.list({});

  requestCalendar.execute(function(resp){
      var calendars = resp.items;
      appendPre('calendars:');
      for(var j = 0; j < calendars.length; j++){
        var calendar = calendars[j];
        var txt = calendar.summary + '   ' + calendar.colorId + ' = ' + calendar.backgroundColor + '--' + calendar.foregroundColor;
        // appendPre(calendar.id + ':' + txt);

        var fun = function(){
            var id = calendar.id;
            var mycal = calendar;
            var fun1 = function(){
                var request = gapi.client.calendar.events.list({
                    'calendarId': mycal.id,
                    'timeMin': beginDate, //(new Date()).toISOString(),
                    'timeMax': endDate,
                    //'timeMin': (new Date()).toISOString(),
                    'showDeleted': false,
                    'singleEvents': true,
                    'maxResults': 10,
                    'orderBy': 'startTime',
                    'items': 'colorId',
                    'fields': 'items(colorId,summary,start,end,id)'
                  });

                  function req(resp) {
                    var events = resp.items;
                    if (events.length > 0) {
                        for (i = 0; i < events.length; i++) {
                            var event = events[i];
                            var when = event.start.dateTime;
                            if (!when) {
                              when = event.start.date;
                            }
                            if(dateEvents.indexOf(event.summary) < 0){
                                appendPre(mycal.summary  +'\t' + mycal.backgroundColor + '\t' + event.summary + '\t (' + when + ')\t')
                            }
                            else{
                                appendPre(mycal.summary  +'\t#dcf1db\t' + event.summary + '\t (' + when + ')\t')
                              }
                            if(!lsResult[mycal.id])lsResult[mycal.id] = [];
                            lsResult[mycal.id][lsResult[mycal.id].length] = {'color': mycal.backgroundColor, 'desc': event.summary};
                        }
                    }
                    else {
                        appendPre('No upcoming events found.');
                    }
                  }
                  request.execute(req);
            }
            return fun1;
        }
        fun()();
      }
  })
}

/**
 * Append a pre element to the body containing the given message
 * as its text node.
 *
 * @param {string} message Text to be placed in pre element.
 */
function appendPre(message) {
  var pre = document.getElementById('output');
  var textContent = document.createTextNode(message + '\n');
  pre.appendChild(textContent);
}


function parseURL(url) {
    var a =  document.createElement('a');
    a.href = url;
    return {
      source: url,
      protocol: a.protocol.replace(':',''),
      host: a.hostname,
      port: a.port,
      query: a.search,
      params: (function(){
        var params = url.split('?')[1].split('&');

        var ret = {};
        for (i = 0; i < params.length; i++) {
          if(params[i].indexOf('=')<0)continue;
          s = params[i].split('=');
          ret[s[0]] = s[1];
        }
        return ret;
      })(),
      file: (a.pathname.match(/\/([^\/?#]+)$/i) || [,''])[1],
      hash: a.hash.replace('#',''),
      path: a.pathname.replace(/^([^\/])/,'/$1'),
      relative: (a.href.match(/tps?:\/\/[^\/]+(.+)/) || [,''])[1],
      segments: a.pathname.replace(/^\//,'').split('/')
    };
}

```