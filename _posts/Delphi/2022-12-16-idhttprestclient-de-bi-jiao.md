---
layout: post
title: "idhttp，restclient的比较"
description: "jekyll的theme是咋回事，好复杂"
category: "Delphi"
modified: 2022-12-16 00:09
tags: "idhttp restclient unigui"
---
* content
{:toc}

Delphi下的http请求
---
>说白了，不管是什么语言，都还是要遵循http规范。
都不过是一个普通的http客户端而已，至于是用chrome，还是我们自己写的代码。
想清楚这点，很容易就明白了。我们不过是发个请求，处理个响应而已。曾经试过用Api 直接写，发现升级改造很麻烦，idhttp处理http异常不太好，如果复杂的认证也有点费劲，NTLM，sftp之类，可以用IpWorks，如果纯粹是json，可以用restclient，用下来还挺好的。





# 1.idhttp
用得比较多的是idhttp，也用习惯了。最近发现它不能很好处理http异常。所以找了一些其他的办法。
这里说的不能很好处理是指，http返回的不是200，而是400之类的，在默认情况下，idhttp认为是正常的，但是我们的业务逻辑上已经出问题了。
老牌控件了，这个以前是第三方的，后来应该是纳入产品了。从D7开始一直用这个东西，也算是熟门熟路了。

### 基础使用

{% highlight pas %}
uses idhttp;

proceudre TestHttp;
var
    AIdhttp: TIdHttp;
    strReturn: string;
begin
    AIdhttp := TIdhttp.Create;
    try
        strReturn := AIdhttp.Get('http://bing.com');
        ShowMessage(strReturn);
    finally
        AidHttp.Free;
    end;
TIdHTTP.Create;
end;
{%  endhighlight   %}

### get和post

http的基础知识不再赘述，在Rest风靡之前，主要是Get和Post，其他的其实也差不多。
get就是上面的例子，Post多一个请求参数。

{% highlight pas %}
uses idhttp;

proceudre TestHttp;
var
    AIdhttp: TIdHttp;
    strReturn: string;
    lsParam: TStringList;
    SS: TStringStream;
begin
    AIdhttp := TIdhttp.Create;
    lsParam := TStringList.Create;
    lsParam.Values['user'] := 'user1';
    lsParam.Add('age=2');
    // 这2种方式都可以，个人比较喜欢前面的，编辑更方便一点。
    SS := TStringStream.Create('', TEncoding.GetEncoding(65001));
    try
        AIdhttp.Post('http://bing.com', lsParam, SS);
        SS.Position := 0;

        ShowMessage(SS.DataString);
    finally
        SS.Free;
        lsParam.Free;
        AidHttp.Free;
    end;
TIdHTTP.Create;
end;

{%  endhighlight   %}

> 这里的小技巧，主要是Position重置比较稳妥。另外是关于字符集的。基本上主流服务器多数是Utf-8，编码问题主要针对东亚文字比较多见一些。可能和个人的项目经验有关。

### 带上cookie
很多服务器都是通过cookie来验证。
回到根本上来说，我们就是要组装一个结构，发给服务器。
这个结构有header，也有body。

body我们放在Post里面了，所以主要是Header.
Delphi如果要做验证的事，可用的资料并不多，如果是特别复杂的验证，比如NTLM,还是有点复杂的。
这里主要介绍简单的状况。
一般来说，我们第一次Post，登录以后，服务器的返回信息里面，会有一个Header.
在Idhttp.Response里面，通过 Set-cookie 传递给客户端，如果浏览器就自己写了，我们就需要把它弄出来。
比如java应用的  sessionid 之类的。
我们下次请求的时候，带上 cookie，就能正常访问了。

``` Delphi
uses idhttp;

IdHTTP1.Request.CustomHeader.Values['cookie'] := xxx;

```

实际情况并不需要这么去操作，只是说明一下，我们的Header都可以通过这个方式来处理。
有些服务器需要额外的请求头，我们就可以通过这个来处理，大部分的通用属性idhttp 都好了。

> 有些自研的服务器，通过token来认证，这个token如果在Get请求里面带，就要通过上面的方法，给CustomHeader来弄了。

而前面提到的Cookie的处理，可以通过CookieManager来处理
{% highlight pas %}
uses idhttp;

proceudre TestHttp;
var
    AIdhttp: TIdHttp;
    strReturn: string;
    cmAuth : TidCookieManager;
begin
    AIdhttp := TIdhttp.Create;
    AIdhttp.AllowCookie := True;
    cmAuth := TidCookieManager.Create;
    idHttp.CookieManager := cmAuth;
    try
        AIdhttp.Get('http://bing.com');
    finally
        AidHttp.Free;
    end;
TIdHTTP.Create;
end;

{%  endhighlight   %}

### https
https里面一般默认用就可以了，很特殊的情况才需要设置ssl的版本。也就是下面的Method。
{% highlight pas %}
Var
  
  IdHttp : TIDHttp;
  IdSSL : TIdSSLIOHandlerSocketOpenSSL;
begin
  idhttp := TIdhttp.Create;
  IdSSL := TIdSSLIOHandlerSocketOpenSSL.Create(nil);
  idHttp.IOHandler := idSSL;
  idHttp.Get('https://bing.com');
  idSSL.SSLOptions.Method := sslvTLSv1;
  idSSL.SSLOptions.Mode := sslmUnassigned;
  
end;
{%  endhighlight   %}

需要注意的是，ssl的dll要放在它能找到的地方，当前目录，或者是system32目录。


### 解压br还没有
以前没有注意解压这个事，现在很多服务器为了减少带宽占用，会启用压缩。
``` bash
accept-encoding: gzip, deflate, br
```
这句话的意思是告诉服务器，这3种压缩方式我都ok，服务器就会按优先级整。
比如，服务器3种都支持，我们告诉它，我只能接受 gzip，它就会发gzip的内容给我们。
但是如果说我们都支持，它可能就发 br的格式了。
以前没太在意，最近才开始了解，目前了解的情况是，idhttp默认情况下，br不太好解。前面2种都可以。测试可能是因为br压缩比例更高。

{% highlight delphi %}

uses
    IdCompressorZLib;

var
  strReturn: string;
  SS: TStringStream;
  Compressor: TIdCompressorZLib;
begin

  FIdHttp.Request.AcceptEncoding := 'gzip, deflate';
  FIdHttp.AllowCookies := True;

  Compressor := TIdCompressorZLib.Create;
  SS := TStringStream.Create('', TEncoding.GetEncoding(65001));
  try
    FIdHttp.Compressor := Compressor;   // 关键就在这里了
    FIdHttp.Post('https://bing.com', SS);
    SS.Position := 0;
    strReturn := SS.DataString;
  finally
    SS.Free;
    Compressor.Free;
  end;

end;

{%  endhighlight   %}



# 2.restclient
因为idhttp的状况，打算

### 基础使用

# 3.IPWorks

处理复杂的验证，比如sftp等情况，idhttp的复杂度就有点高了，可以看看这个


# 4.工具


# 总结一些
* 用restclient还有个好处，在unigui里面，fiddle可以捕获，idhttp好像不行
* idhttp如果连https，需要dll文件
* 如果有兴趣可以直接用Api 自己实现，体量会小一些，但是升级改造还是太累了
