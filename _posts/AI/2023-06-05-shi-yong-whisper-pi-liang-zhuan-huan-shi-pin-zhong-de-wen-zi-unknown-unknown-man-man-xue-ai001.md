---
layout: post
title: "使用Whisper批量转换视频中的文字——慢慢学AI001"
description: ""
category: "AI"
modified: 2023-06-05 23:45
tags: "python whisper video"
---
* content
{:toc}

> 因为工作需要把视频中的语音转换成文字，网上找了很多方案，效果不佳不说，大部分都是价格不菲。正好最近在学习OpenAI，于是找到了这款神器，意外的效果好，而且免费，而且本地就能运行。它有一个windows下客户端可以直接使用，但是一次只能处理一个文件，所以就想着如何自动化批量处理，发现原来它有个cli版本。
总的来说，它的原理是先通过ffmpeg转换成音频文件，然后再通过whisper转换成文字
![](../../images/2023-06-05-23-52-09.png)


<!-- more -->
# 1、去哪里下载
https://github.com/openai/whisper/releases
在github上可以下载到最新的版本

很好理解，模型越大越慢，也越精准，所以我下载了large

# 2、客户端版本

# 3、Python实现（调用cli命令，最终版）

> 通过cli命令是因为它和客户端版是一起的，而客户端版使用了gpu，并且输出效果很好。

### 3.1 基本配置

### 3.1 实现代码

``` python


```

### 3.3 命令说明
基本使用方法如下
> whispercli.exe [options] file0.wav file1.wav ...

我们使用命令行参数带 --help 的时候，比较特别的是，第3列代表着当前的值，也许是我们上次执行之后留下来的值，不知道它保存在哪里，有时候确实会轻松一点

|简写|完整写法|当前值|说明|
|----|----|-----|-----|
|  -h,       |--help          |[default] |show this help message and exit
|  -la,      |--list-adapters |系统中当前的显卡名，给后面的参数用
|  -gpu,     |--use-gpu       |使用gpu加速，这里后面跟的是显卡的名字，
|  -t N,     |--threads N     |[4      ] |number of threads to use during computation
|  -p N,     |--processors N  |[1      ] |number of processors to use during computation
|  -ot N,    |--offset-t N    |[0      ] |time offset in milliseconds
|  -on N,    |--offset-n N    |[0      ] |segment index offset
|  -d  N,    |--duration N    |[0      ] |duration of audio to process in milliseconds
|  -mc N,    |--max-context N |[-1     ] |maximum number of text context tokens to store
|  -ml N,    |--max-len N     |[0      ] |maximum segment length in characters
|  -wt N,    |--word-thold N  |[0.01   ] |word timestamp probability threshold
|  -su,      |--speed-up      |[false  ] |speed up audio by x2 (reduced accuracy)
|  -tr,      |--translate     |[false  ] |从原始语音翻译成英文
|  -di,      |--diarize       |[false  ] |stereo audio diarization
|  -otxt,    |--output-txt    |[false  ] |以txt的方式输出，说白了就是没有时间轴信息了，这个符合我的需求
|  -ovtt,    |--output-vtt    |[false  ] |output result in a vtt file
|  -osrt,    |--output-srt    |[false  ] |output result in a srt file
|  -owts,    |--output-words  |[false  ] |output script for generating karaoke video
|  -ps,      |--print-special |[false  ] |print special tokens
|  -nc,      |--no-colors     |[false  ] |do not print colors
|  -nt,      |--no-timestamps |[false  ] |不要输出时间轴信息，默认是关闭的，就是一行信息，最前面是时间
|  -l LANG,  |--language LANG |[en     ] |这里指的是输入的音频文件，讲的是啥语音，用的是zh
|  -m FNAME, |--model FNAME   |[models/ggml-base.en.bin] |model path
|  -f FNAME, |--file FNAME    |[       ] |输入的文件名，这里大家可以看到，它是音频文件不是视频问题，所以需要转换

* lang 有时候出来是繁体中文，但是都用的是zh

# 4、Python实现（调用openai，失败了）

想到用这个方案，是因为纯pyhon调用openai的方法失败了，主要是卡在2个问题上
* 没有调用gpu，使用cpu特别慢
* 一直报错，可能是因为

如何看是否启用了gpu，在windows下很容易从任务管理器里面看，最后会发现特别慢

这里一直报文件不存在，换了几个方法

不用ffmpeg，用ffmepg-python也不行

# 5、异常信息和解决方法