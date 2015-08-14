---
layout: post
title: "道听途说Domino管理3 - 获取数据库限额"
description: "通过命令获取数据库相关信息，限额等"
category: "Domino管理"
modified: 2015-06-08 14:16
tags: "Domino管理 数据库限额 show directory"
---
{% include JB/setup %}
# 1.问题背景
有一个需求，要统计所用用户的邮件大小和限额，并导出成报表

# 2.尝试方案
第一个想到的方案，是通过NotesDatabase对象，获取数据库属性等。具体方法有2种：

* 通过NotesDbDirectory遍历。

{% highlight vbnet %} 

Sub Initialize  

	Dim session As New NotesSession
	Dim db As NotesDatabase
	
	Dim directory As NotesDbDirectory 
	Set directory = New NotesDbDirectory("test/test") 
	Set db = directory.GetFirstDatabase( Database ) 

	Dim dbMax As Double
	Dim dbSize As Double
		
	Do While Not (db Is Nothing) 
		On Error Resume Next 
		'Call db.OpenMail 'you have to open the db to get the size property 
		dbmax = (db.sizequota)/1024 'puts quota into Megs 
		
		dbsize = (db.size)/1024 'puts size into kb 
		dbsize = Round( (dbsize/1024), 0 ) 'puts size into mb, rounds to nearest Integer 

		MsgBox db.Filepath + " -- " + CStr(dbsize)
		
		Set db = directory.GetNextDatabase 'get the next database 
	Loop 
	
End Sub  
{% endhighlight %} 


这里有一个比较有意思的，如果加了

{% highlight vbnet %}   
Call db.OpenMail   
{% endhighlight %} 

数据库路径就一直是当前用户

* 通过Names库的视图，获取用户文档

做法相差不大，相对NotesDbDirectory多了一个视图和文档的开销。

问题是什么呢。 

**这2种方式都需要运行代理的人，需要有权限获取这个数据库**

# 3.当前方案
基于前面的尝试（心里还是很不甘心的，先解决问题吧）。想起来为什么WebAdmin可以获取这些数据库大小。然后开始扒拉代码。因为是要获取限额，所以直接搜索quota就找到了。

原理其实比较简单，直接通过控制台命令

{% highlight bash %}  
show directory 目录 -xml
{% endhighlight %}

就可以了。

* 如果最后没有-xml，结果会比较简单。

 {% highlight bash %} 
Show Directory	  
{% endhighlight %}

[017E:0003-01CF] | DbName | Version|Logged
:----------- | :-----------: | -----------: | :------------:
[017E:0003-01CF]         | f:\notefile\schema50.nsf        | V5:41|Yes
[017E:0003-01CF]         | f:\notefile\Stats.box        | V5:27|No



* 用了-xml，结果大致如下：
 {% highlight xml %}  
<?xml version="1.0" encoding="UTF-8" ?>
<files xmlns="http://www.lotus.com/dxl/console">
 <filedata notesversion="8" odsversion="51" logged="disabled" backup="no" id="48257E59:00313CF5"  link="1" dboptions="268443648,21626880,57348,0">
  <replica id="48257873:001E7AEF" flags="56" count="1">
   <cutoff interval="90">20150217T025339,84+08</cutoff>
  </replica>
  <path>/notesdata/mail/test1.nsf</path>
  <name>test1.nsf</name>
  <title>test1</title>
  <template></template>
  <inheritedtemplate>Mail6</inheritedtemplate>
  <category></category>
  <size current="2643984384" max="0" usage="2640352256"/>
  <quota limit="0" warning="0"/>
  <created>20150603T165748,69+08</created>
  <lastcompact></lastcompact>
  <unread marks="yes" replicate="never"/>
  <daos enabled="no"/>
  <pirc enabled="no"/>
 </filedata>
 <filedata notesversion="8" odsversion="51" logged="disabled" backup="no" id="48257E3B:002BE00F"  link="1" dboptions="0,21626880,108774,0">
  <replica id="48257E3B:002BDB28" flags="8" count="1">
   <cutoff interval="90">20150306T022916,12+08</cutoff>
  </replica>
  <path>/notesdata/mail/test2.nsf</path>
  <name>test2.nsf</name>
  <title>test2</title>
  <template></template>
  <inheritedtemplate>StdR85Mail/zh-CN</inheritedtemplate>
  <category></category>
  <size current="13369344" max="0" usage="13093888"/>
  <quota limit="0" warning="0"/>
  <created>20150504T155914,07+08</created>
  <lastcompact></lastcompact>
  <unread marks="yes" replicate="all"/>
  <daos enabled="no"/>
  <pirc enabled="no"/>
 </filedata>
{% endhighlight %}

从这个结构里面，我们其实获取了数据库的当前大小和限额，速度非常快。有了这个结构以后，就需要开始解析xml。

lotusscript的解析其实是比较怪异的，下标是从1开始的。

下面是主角登场，阉割过的版本，如果找不到完整的，可以联系我。
{% highlight vbnet %} 
Const CONSOLE_XML			= "-xml"

Private Type TypeFileData
	sPath			As String
	sName			As String
	
	dSize			As Double
	dSizeUsed			As Double
	lSizeMax			As Long
	lQuotaLimit		As Long
	lQuotaWarning		As Long
	
End Type

Private Class cFileData
	Private m_session As NotesSession
	
	Public Sub New
		On Error GoTo ERROR_HANDLER
		Set m_session = New NotesSession
		
		
		Exit Sub
ERROR_HANDLER:
		Exit Sub
		
	End Sub	
	
	public Sub GetDirectoryData(sServer As String , sPath As String,lsDB List As TypeFileData )
		
		On Error GoTo ERROR_HANDLER
		
		Dim tFD	 			As TypeFileData
		
		Dim sResponse			As String
		Dim sCmd				As String
		
		Dim DOMParser			As NotesDOMParser
		Dim DOMDocument		As NotesDOMDocumentNode
		Dim DOMAttributes		As NotesDOMNamedNodeMap
		Dim DOMNodeList		As NotesDOMNodeList
		Dim DOMNode			As NotesDOMNode
		
		Dim sAttribName		As String
		Dim sAttribText		As String
		Dim sNodeName			As String
		Dim sNodeText			As String
		
		Dim lNodeIndex			As Long
		Dim lAttribIndex		As Long
		Dim iIndex			As Integer
		
		Dim CONSOLE_PREFIX As String 
		
		sCmd		= CONSOLE_PREFIX + |show directory "| + sPath + |" | + CONSOLE_XML
		sResponse	= m_session.SendConsoleCommand(sServer, sCmd)
		
		
		Set  DOMParser	= m_session.CreateDOMParser
		Call	DOMParser.Setinput(sResponse)
		Call	DOMParser.Process()
		Set	DOMDocument = DOMParser.Document
		
		Set DOMNodeList	= DOMDocument.GetElementsByTagName("filedata")
		For lNodeIndex = 1 To DOMNodeList.NumberOfEntries
			
			tFD.sPath			= ""
			tFD.sName			= ""
			
			
			tFD.dSize			= 0
			tFD.dSizeUsed		= 0
			tFD.lSizeMax		= 0
			tFD.lQuotaLimit	= 0
			tFD.lQuotaWarning	= 0
			
			'loop all child nodes of <filedata>  
			Set DOMNode = DOMNodeList.GetItem(lNodeIndex).FirstChild
			Do While Not DOMNode.isNull
				
				If DOMNode.nodeType = DOMNodeType_Element_Node Then
					
					sNodeName = DOMNode.nodeName
					Select Case sNodeName	
					Case "size":
						
						Set DOMAttributes = DOMNode.Attributes
						For lAttribIndex = 1 To DOMAttributes.NumberOfEntries
							sAttribName = DOMAttributes.GetItem(lAttribIndex).NodeName
							sAttribText = DOMAttributes.GetItem(lAttribIndex).NodeValue
							Select Case sAttribName
							Case "current":	tFD.dSize 		= CDbl(sAttribText)
							Case "usage":		tFD.dSizeUsed		= CDbl(sAttribText)
							Case "max":		tFD.lSizeMax		= CLng(sAttribText)
						End Select
						Next lAttribIndex
						
					Case "quota":
						
						Set DOMAttributes = DOMNode.Attributes
						For lAttribIndex = 1 To DOMAttributes.NumberOfEntries
							sAttribName = DOMAttributes.GetItem(lAttribIndex).NodeName
							sAttribText = DOMAttributes.GetItem(lAttribIndex).NodeValue
							Select Case sAttribName
							Case "limit":		tFD.lQuotaLimit	= CLng(sAttribText)
							Case "warning":	tFD.lQuotaWarning	= CLng(sAttribText)
						End Select
						Next lAttribIndex
						
				End Select
					
					'textual values of a node are stored off in a childnode
					If DOMNode.HasChildNodes Then
						
						sNodeText = DOMNode.firstChild.nodeValue
						
						Select Case sNodeName
						Case "path":				tFD.sPath			= sNodeText
						Case "name":				tFD.sName			= sNodeText
						Case "title":				tFD.sTitle 		= sNodeText
						Case "template":			tFD.sTemplate		= sNodeText
						Case "inheritedtemplate":	tFD.sTemplInherited	= sNodeText
						Case "category":			tFD.sType			= sNodeText	
					End Select
						
					End If
					
				End If	
				
				Set DOMNode = DOMNode.NextSibling
					
				
				lsDB(sServer + tfd.sName).dSize = tfd.dSize
				lsDB(sServer + tfd.sName).dSizeUsed = tFd.dSizeUsed
				lsDB(sServer + tfd.sName).lQuotaLimit = tFd.lQuotaLimit
				lsDB(sServer + tfd.sName).sPath = tFd.sPath
				lsDB(sServer + tfd.sName).sName = tFd.sname
				lsDB(sServer + tfd.sName).lSizeMax	 = tFd.lSizeMax
				lsDB(sServer + tfd.sName).lQuotaWarning = tFd.lQuotaWarning
					
			Loop
		Next lNodeIndex
	Exit Sub
			
ERROR_HANDLER:	
	Exit Sub
			
   End Sub
	

	
End Class

{% endhighlight %} 

如何使用，其实比较简单，
{% highlight vbnet %} 
Dim fd As New cFileData
Dim lsFD List As TypeFileData
Call fd.GetDirectoryData("mailserver", "mail", lsFD)
msgbox lsFD("test1.nsf").sName + "  -----"
	
{% endhighlight %} 