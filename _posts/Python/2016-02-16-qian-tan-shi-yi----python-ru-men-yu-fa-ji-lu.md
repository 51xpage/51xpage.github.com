---
layout: post
title: "浅滩拾遗 - Python入门语法记录"
description: "Python的入门语法记录"
category: "Python"
modified: 2016-02-16 15:59
tags: "python dict for 数组"
---
{% include JB/setup %}

1. 批量注释

“”“

2. 私有方法/保护方法

  _ 保护方法  
  __ 私有方法

3. 数组遍历处理

   {% highlight python %} 
   lst = [n for n in range(5, 10)]
   >>> print(lst)

   data = [a.nextSibling.next.string for a in soup.select("table tr td[width=17%]")]
   {% endhighlight %} 
   获取td，前面的那个表达式是用来处理下一个下一个什么什么的，最后是string相当于就是innerHTML

4. 数组元素获取

   {% highlight python %} 
   L[1:]
   L[1:2]
   L[2]
   L[-2]
   {% endhighlight %} 
   
5. dict合并

   {% highlight python %} 
   dict({"productid": productid, "storeid": storeId, 'userid':'userid'},**(_json['requestObj']))
   {% endhighlight %} 


6. 格式化时间

   {% highlight python %} 
   import datetime
   datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

   import time
   time.time()
   {% endhighlight %} 
   
7. 有序/无序

   {% highlight python %} 
   new_items = [x if x != None else " " for x in data]
   new_items = （x if x != None else " " for x in data）
   {% endhighlight %} 

8. 返回结果居然可以是多个！

   {% highlight python %} 
   (a, b) = xxxxxx()
   {% endhighlight %} 
   返回结果可以直接用a和b变量了

9. join 比较奇怪，字符串在前面
