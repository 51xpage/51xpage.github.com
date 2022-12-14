---
layout: post
title: "浅滩拾遗 - Node.js+MongoDb开发环境搭建"
description: "Mac下搭建node.js的开发环境"
category: "Node.JS"
modified: 2015-07-30 11:54
tags: "Node Node.js MongoDB brew npm"
---
"test-jb-setup"
#1、配置环境

	**配置只针对Mac**

##1.1、安装brew
一个安装工具，简单理解类似apt-get。想装什么一个命令就装上了，不用再去下载了。

在终端执行下面的语句就安装好了

{% highlight bash %} 
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 
{% endhighlight %}

简单命令  
检查当前装了哪些应用
{% highlight bash %} 
brew list
{% endhighlight %}

安装某个应用  
{% highlight bash %} 
brew install xxx
{% endhighlight %}

卸载某个应用  
{% highlight bash %} 
brew uninstall xxx
{% endhighlight %}

##1.2、安装node和mongodb
有了brew打底，直接

{% highlight bash %}   
brew install node  
brew install mongodb  
{% endhighlight %}

##1.3、安装依赖包
node.js有自己的包管理方案，即npm，通过它很容易就可以安装卸载依赖。
这里的依赖简单理解就是现成的js库，实现特定功能。和jar包不太一样，它是源码形式的。而为了管理依赖关系，一个node工程会有一个package.js的文件，如：

{% highlight json %} 
{
  "name": "test",
  "version": "2.0.0",
  "description": "Test",
  "main": "index.js",
  "scripts": {
    "start": "node ./start.js",
    "test": "node ./index.js"
  },
  "author": "xxx",
  "license": "ISC",
  "dependencies": {
    "express": "^4.13.4",
    "express-restify-mongoose": "^1.0.7",
    "lodash": "^3.9.3"
  },
  "devDependencies": {
  }
}
{% endhighlight %}

在它所在文件夹下执行
{% highlight bash %} 
npm install
{% endhighlight %}

即可安装所有的依赖，所有的包都会下载到相同目录的**node_modules**文件夹下。如果需要单独安装，可以在install后面带参数，如  
{% highlight bash %} 
npm install xxx
{% endhighlight %}

##1.4、安装调试工具
node.js的调试方法很多，这次用到的是node-inspector，安装很简单。如下
{% highlight bash %} 
npm install -g node-inspector
{% endhighlight %}

使用它可以直接在chrome里面调试node.js

#2、如何调试
#2.1 以debug模式启动
{% highlight bash %} 
node --debug-brk=5858 start.js
{% endhighlight %} 
这样就启动了debug模式了

#2.2开启inspector
{% highlight bash %} 
$ node-inspector 
Node Inspector v0.11.1
Visit http://127.0.0.1:8080/?ws=127.0.0.1:8080&port=5858 to start debugging.
{% endhighlight %} 

# 2.3 调试工具
比较推荐2个，都是chrome插件

* Advanced Rest Client Application
* Postman

个人更喜欢前一个，可能用的比较早的原因


#3、MongoDB简单使用
#3.1 启动
{% highlight bash %} 
mongod --config /usr/local/etc/mongod.conf --auth
{% endhighlight %} 
最后这个--auth用于验证，稍微麻烦点，本就不用开了

#3.2 查询删除
* 连接  
{% highlight bash %} 
mongo 127.0.0.1:27017
{% endhighlight %} 
* 查看数据库列表
{% highlight bash %}
show dbs 
{% endhighlight %}
* 使用数据库 
{% highlight bash %}
use xxxx 
{% endhighlight %}
* 查看表 
{% highlight bash %}
show collections 
{% endhighlight %}
* 查询 
{% highlight bash %} 
db.xxxxx.find()
{% endhighlight %} 
* 删除库
{% highlight bash %} 
db.dropDatabase()
{% endhighlight %} 
 

#3.3 三方工具
推荐Robomongo和Mongo Management Studio，大同小异