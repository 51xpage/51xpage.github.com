---
layout: post
title: "道听途说Jenkins系统8 - 发布到maven"
description: "如何发布到maven服务器"
category: "配置管理"
modified: 2015-10-06 21:12
tags: "jenkins maven"
---
{% include JB/setup %}
# 1、Maven理解
  做Java开发是一个非常繁琐的过程。有很多步骤需要手工处理，包括包的管理，包的依赖，产品的发布，工程的管理等等。也出现了很多工具来实现管理工作。包括Ant等等。  
  另外一个Java工程，很大的体积占用都是引用的Jar包，而这些Jar包的管理会是一个很大的挑战。实际上完全可以独立成由专门的服务器来管理各个Jar包。  
  简单理解，就是针对项目要做的时候，做一个自动化的批处理文件（bat或者sh文件），而项目各不相同，所以就有不同的批处理。所以有了自动化管理的工具，抽象项目管理，发布，构建的各个阶段，通过一个统一的规范。
  基本功能如下： 

* 包管理
* 自动化构建发布 

		java的很多管理工具都是通过xml来描述，规范

我们知道，按照管理，maven作为一个工具，配合工具运行有全局的配置以及符合项目本身的配置

### 1.1、settings.xml

settings.xml是全局配置，放在/etc/maven/settings.xml或者 ~/.m2/settings.xml。通过调试会发现系统会先读取etc目录下的内容，然后去看~/.m2下有没有，有的话就用~/.m2下的内容。
它由几个部分组成：

1. <localRepository/>
	本地库，简单说，项目用到的jar包都会放到这里，而不是项目文件夹下面。这样项目文件夹就比较干净。做版本管理也比较好。
2. <interactiveMode/>
    没用过，跳过
3. <usePluginRegistry/>
	没用过，跳过
4. <offline/>
	没用过，跳过
5. <pluginGroups/>
	插件？没用过，跳过
6. <servers/>
	重点来了，这里指定maven的库，简单理解就是放jar包的地方。项目初始的时候，有人把一些jar包放上去，项目从上面下载即可。里面可以放多个地址。
	* id>server001，服务器id，
	   这个id非常重要，对应pom.xml中的distributionManagement对应的id
	* username>my_login
    * password>my_password
    * privateKey>${user.home}/.ssh/id_dsa
    * passphrase>some_passphrase
    * filePermissions>664
    * directoryPermissions>775
	
7. <mirrors/>
	可能是镜像，不懂
8. <proxies/>
	代理服务器，为了连上面的东西用的
9. <profiles/>
	远程仓库列表，它是Maven用来填充构建系统本地仓库所使用的一组远程项目。有了nexus等，应该来说就不用了，而nexus的设置在pom里面做过了，所以可以简单点
	
	{% highlight xml %}
	<repository>
          <id>codehausSnapshots</id>
          <name>Codehaus Snapshots</name>
          <releases>
            <enabled>false</enabled>
            <updatePolicy>always</updatePolicy>
            <checksumPolicy>warn</checksumPolicy>
          </releases>
          <snapshots>
            <enabled>true</enabled>
            <updatePolicy>never</updatePolicy>
            <checksumPolicy>fail</checksumPolicy>
          </snapshots>
          <url>http://snapshots.maven.codehaus.org/maven2</url>
          <layout>default</layout>
        </repository>
      </repositories>
      {% endhighlight %}
	
	这里的releases和snapshots没搞懂啥意思，也不知道咋匹配用户名密码的。
	
10. <activeProfiles/>
    表示那个是激活的，没啥。
    
    从上面的配置来看，平常用得比较多的，是库的位置和对应的用户名

### 1.2、pom.xml

上面提到settings.xml其实最关键的设置就一个，server部分。然后我们看看pom.xml（项目对象模型， Project Object Model），它在项目文件夹下面是maven的沟通文件。它主要由如下几个部分组成：

* 项目依赖dependencies  
	表示当前项目用到的jar包
* 项目引用库repositories
	maven会把上面项目依赖设定的内容，从引用库中拉下来
* dependencyManagement
* modules
* distributionManagement
	这里涌来表示要发布到maven服务器的地址
	
{% highlight xml %}
 <repository>
            <id>xxx</id>
            <name>xxx Repository</name>
            <url>hxxxx1/nexus/content/repositories/releases/</url>
        </repository>
		<snapshotRepository>
			<id>xxx</id>
			<name>xxx Repository</name>
			<url>uxxxs/content/repositories/releases/</url>
		</snapshotRepository>
{% endhighlight %}		


参考<http://blog.csdn.net/ithomer/article/details/9332071>

### 1.3、常用命令

安装
{% highlight bash %}   
mvn install
{% endhighlight %}

发布，大概意思是发布到maven的repository服务器上吧
{% highlight bash %}   
mvn deploy
{% endhighlight %}

### 1.4、调试
maven安装问题比较容易解决，使用的时候，我们可以开启调试。
开启调试非常简单。  
{% highlight bash %}
mvn deploy -X
{% endhighlight %}
如果嫌结果太多，可以换成-X

从这里可以定位异常。

# 2、Jenkins全局配置
jenkins本质上还是调用服务器的功能，所以有前面的maven知识打底是很有必要的。不过好像没啥特别可配置的。可以配置参数，如-X。另外

另外还有一个seetings.xml的地方，在Maven Configuration

当然毫无意外的，它也可以帮忙安装maven


# 3、项目配置
相对而言，项目的配置对复杂很多。

### 3.1、Invoke Top-Level Maven target

这里会设置goals，即上面说的deplay，install等目标，以及settings.xml等

### 3.2 Build
这俩好像重复了吧…… 
里面可以设置goals，参数等等


# 4、nexus配置
因为需要把编译的结果放到服务器，所以需要在nexus上注册一个账号，权限比较简单。
在nexus里面注册一个用户jenkins，权限是Maven的repo all maven repositories（Full Control）
但是光这个权限无法Web登陆，后来加了一个Deployment的啥权限


# 5、开始吧
第一次编译会很慢，因为它从git上拉过来的源码没有jar包，所以maven会去下载jar包，然后这个过程是比较慢的。

Poll SCM，这个设置比较好玩，怎么玩的不知道，
H 20 * * *，

Build periodically，定时更新

# 6、参考资料

<http://p.primeton.com/articles/53b3d567e1382374a6000002>
<http://www.level2crm.com/2015/01/git-maven-jenkins-gitlab-nexus/>
<http://www.cnblogs.com/leefreeman/p/4211530.html>
<http://www.cnblogs.com/leefreeman/p/4226978.html>
<http://www.sonatype.org/nexus/2015/03/13/jenkins-to-nexus-with-git-polling/>
<https://support.sonatype.com/entries/21283268-Configure-Maven-to-Deploy-to-Nexus>


常见问题
<http://www.java-tutorial.ch/maven/maven-release>


