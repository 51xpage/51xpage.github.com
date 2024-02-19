---
layout: post
title: "道听途说Linux系列10 - shell脚本编程"
description: "Linux下shell编程基础"
category: "服务器管理"
modified: 2015-12-29 15:50
tags: "linux shell 循环 函数 文件包含"
---
"test-jb-setup"

shell脚本在运维中非常实用，但是也因为是脚本语言，书写调试等方面都会比较困难。以下记录学习过程中用到的内容。当然下面介绍的应该是基于bash的，曾经用过AIX下面的ksh，不太习惯。

## 1. 如何编写和运行脚本

   应景，shell脚本以sh为扩展名，实际上这个没关系。只要有执行权限即可。  
   {% highlight bash %}   
   vi xxx.sh     
   chmod +x xxx.sh      
   ./xxx.sh      
    {% endhighlight %} 

## 2. 如何传递参数和获取参数
 
参数传递比较简单，命令行后面用空格分开就可以，如

{% highlight bash %}     
    ./xxx.sh 参数1  参数2   
{% endhighlight %} 
 
脚本中如果要使用通过$符号加序号即可获取，如

{% highlight bash %}  
param1=$1  
param2=$2  
……  
{% endhighlight %} 
## 3. 变量使用  

   从上面我们看到变量其实可以简单的用 $ 显示，变量的定义比较简单，直接设置即可，引用的时候需要用$包裹，如
   
  {% highlight bash %}     
      var1=test  
echo $var1  
echo ${var1}  
  {% endhighlight %}   
  
  从上面可以看出来，用 $ 或者 ${} 加变量名都可以，建议包裹一下，不容易混起来。  

  **注意事项**
  
   *  变量声明的时候，= 前后不能加空格，也比较坑爹的

	如果想把一个命令的执行结果放到变量里面，可以用$()包裹，如  
	{% highlight bash %}    
	 var1=$(ps -ef|grep tomcat)  
	echo ${var1}  
	{% endhighlight %} 

	还有一个比较特别的用法，获取当前脚本里面指定前缀或者后缀的变量，形成一个数组，如

	{% highlight bash %}  
	var1=“var1”  
	var2=“var2”  
	vars=${!var*}    
	echo ${vars}    # var1  var2  
	vars2=${!1@}   # var1  
	{% endhighlight %}  

## 4. 字符串
 
  * 拼接字符串
	  
	在脚本里面字符串拼接倒是比较简单，直接2个变量放一起就行了

	{% highlight bash %}
	var1=$(ps -ef|grep tomcat)  
	echo ${var1}”hello”  
	{% endhighlight %} 

  * 字符串截取
	* 从指定位置开始截取，后面的长度是可选项  
{% highlight bash %}   
var1=“hello”  
echo ${var1:1}  
echo ${var1:1:3}    
{% endhighlight %} 
   
   * 删除指定字符串   

{% highlight bash %}  
	
原始字符串var1: 123heolhhlo   
替换字符串var2: o      
${var1:1}  ==\>  23heolhhlo   
${var1:2:2}  ==\>   3h   
${var1\#*${var2}}  ==\>   lhhlo   
${var1\#*h}  ==\>   eolhhlo   
${var1#\#*$var2}  ==\>   
${var1#\#*h}  ==\>   
==============   
${var1%*$var2}  ==\>   123heolhhl   
${var1%%*$var2}  ==\>   
${var1%%*h}  ==\>   123heolhhlo   
==============   
${var1/h/i}  ==\>   123ieolhhlo   
${var1//h/i}  ==\>   123ieoliilo   
==============   
${var1/%h/i}  ==\>   123heolhhlo   
${var1/${var2}/i}  ==\>   123heilhhlo   
==============   
${var1//${var2}/i}  ==\>   123heilhhli   
${var1/%${var2}/i}  ==\>   123heolhhli   

{% endhighlight %}    

可以用来处理获取文件名，扩展名，路径等等。总的来说，# 表示前缀，% 表示后缀
 
## 5. 数组
脚本写多，多半会碰到需要用到数组的地方，生成数组的方法比较多，用得比较多还是通过其他命令获取出来的。

{% highlight bash %}     
arr=$(ls)   
arr=(1 2 3 4 5)   
{% endhighlight %} 

*  长度获取   
{% highlight bash %}     
echo ${#arr[ @ ]()}   
{% endhighlight %}    

* 获取值   
	下标从0开始   

{% highlight bash %}     
echo ${arr[2]()}   
echo ${arr[*]()}      
{% endhighlight %} 

* 赋值

{% highlight bash %}     
arr[0]()=0   
{% endhighlight %} 

* 删除   

{% highlight bash %}     
unset arr   
unset arr[1]()   
{% endhighlight %}    

## 6. 循环

主要介绍数组循环，
{% highlight bash %}   
for vv in ${arr[@]()}   
do   
echo ${vv}   
done   
{% endhighlight %}    

## 7. 函数

* 基本形式

{% highlight bash %}   
function test(){   
p1=$1   
p2=$2   
return 0   
}   
{% endhighlight %}    

函数如果要有参数，不用在括号里面写，引用的时候，用 $加数字即可，当然也有可能没有，但是变量的作用域默认是全局的，也就是说这个函数里面定义了一个变量，出了函数还能用，如果是局部用，可以在变量前面加 local关键字

* 返回值   
	默认返回就是数字，所以无法返回字符串，一种做法就是通过全局变量来处理
	 
## 8. 文件引用
如果代码很多，需要重复引用，可以整理到一个单独的文件，其他文件包含它即可。引用很简单，文件名前面一个 .即可。

. 文件名

注意这里的空格。文件名可以用相对路径也可以是绝对路径，各有利弊，但是需要注意，相对路径指运行命令的路径。

## 9. 注意事项

使用变量的时候，不要加空格

shell 文件包含

参考资料

[http://see.sl088.com/wiki/Shell\_%E8%B0%83%E7%94%A8sh%E6%96%87%E4%BB%B6%E9%87%8C%E7%9A%84%E5%87%BD%E6%95%B0]()

[http://www.runoob.com/linux/linux-shell-include-file.html]()

[http://arganzheng.iteye.com/blog/1174470]()

[http://www.cnblogs.com/chengmo/archive/2010/10/17/1853356.html]()

shell 返回字符串
http://tinyweb.blog.51cto.com/2462673/982616


[http://www.coder4.com/archives/3853]()



shell如何判断参数是一个文件还是一个文件夹？
if [ -d $1 ];then
   ehco "$1 是目录"
elif [ -f $1 ];then
   echo "$1 是文件"
fi


http://www.cnblogs.com/chengmo/archive/2010/10/02/1841355.html

这里的东西比较全面，特别是字符串相关的


function contains() {
local n=$\#
local value=${!n}
for ((i=1;i \< $#;i++)) {
if [ "${!i}" == "${value}" ](); then
echo "y"
return 0
fi
}
echo "n"
return 1
}

pidc=$(pgrep -f tomcat)
echo "\>\>\>12.jstack\<\<\<" \>\>${filename}
echo "   pid:  "${pidc}", 对应线程情况:" \>\>${filename}
ps -mp ${pidc} -o THREAD,tid,time |awk '{print $2 " "$8}'  |sort|tail -n 6|head -n 4 \>\>${filename}
tidcs=$(ps -mp ${pidc} -o THREAD,tid,time |awk '{print $2 " "$8}'  |sort|tail -n 6|head -n 4|awk '{print $2}')

for tidc in ${tidcs[@]()}
do
  echo "     tid:"${tidc}\>\>${filename}
  ttidc=$(printf "%x\n" ${tidc})
  jstack ${pidc} |grep ${ttidc} -A 100 \>\>${filename}
  echo "     ====="\>\>${filename}
done

echo "============"\>\>${filename}


su - \<user\>  -c "bash -c  'cd $DIR ;\<service name\>'"

shell的服务脚本里面加这个

==

在shell脚本中，无法对浮点数进行比较，如：
max=0.1
min=0.01
if [ "$max" -gt "$min" ]()
then
echo "YES"
else
echo "NO"
fi
这样的比较，运行后得到错误：
line 4: [: 0.1: integer expression expected
]()因为bc和awk都支持浮点数，可以使用bc进行处理：
max=0.1
min=0.01
if [ `echo "$max > $min" | bc` -eq 1 ]()
then
echo "YES"
else
echo "NO"
fi
也可以写成if [ $(echo "$max \< $min"|bc) -eq 1 ]()

http://www.cnblogs.com/sunyubo/archive/2011/10/17/2282047.html
判断文件是否存在

几个坑，因为以前为了代码美观，= 号两头有空格，现在shell公然不支持，

