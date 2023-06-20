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
* 代码下载

https://github.com/openai/whisper/releases
在github上可以下载到最新的版本
>这个是官方的地址，有兴趣可以下来看看，主要用到的是下面地址的内容

* 模型下载（针对命令行方式和客户端方式）

https://huggingface.co/datasets/ggerganov/whisper.cpp/tree/main
![](../../images/2023-06-20-00-29-09.png)

很好理解，模型越大越慢，也越精准，所以我下载了large。

# 2、客户端版本
这里说的客户端版本，就是它提供了一个exe文件，里面可以设置一些东西。
https://github.com/Const-me/Whisper/releases
![](../../images/2023-06-20-00-24-43.png)

这里的WhisperDesktop就是Windows下的版本了，从这里看应该是没有其他系统的版本了。
客户端版本使用比较简单，但是需要先下载模型文件，下面会用到，它启动就会要求。

### 2.1 启动
启动很简单，加载模型需要一些时间，还挺久的
![](../../images/2023-06-20-00-33-39.png)
这里可以设置选择哪个显卡，在advanced里面可以设置显卡
![](../../images/2023-06-20-00-35-46.png)
老实说，也没啥必要调整，就一个简单工具，调整也调不出花来。


### 2.2 转换
![](../../images/2023-06-20-00-39-09.png)
设置一下要转换的文件，还有输出的格式，默认情况，下面的Place that file to the input folder 是没有选中的，选中以后，输出的文件名就和原始文件名一致，但是扩展名不同。
比如图上的，原始文件名是 家庭.mp4,结果就是 家庭.txt。
设置好了以后，就开始走进度转换了

>转换的效果没得说，遗憾的是一次只能搞1个。所以想尝试批量方案。一开始尝试rpa，后来想想有点杀鸡用牛刀了

# 3、Python实现（调用cli命令，最终版）

> 通过cli命令是因为它和客户端版是一起的，而客户端版使用了gpu，并且输出效果很好。

### 3.1 基本配置
下载地址就是上面的那个，cli文件，但是解压以后会发现，它的名字居然叫 main.exe,有点不能忍啊。
反正windows程序，我们简单理解为，在命令行能直接执行的，就在Path里面设置好就行了。
解压到一个地方，把它名字改了。
![](../../images/2023-06-20-00-50-42.png)
它的路径放在c盘下面，加到path里面就可以了

![](../../images/2023-06-20-00-48-24.png)
这个操作有点复杂，意思就是找到系统属性就行了，不同的操作系统，大同小异，基本都是这样

这样弄好了以后，就可以在命令行里面测试了
``` bash
whispercli --help
```

### 3.2 实现代码

``` python
# -*- coding: utf-8 -*-
import os
import subprocess
import time
from tqdm import tqdm

video_directory = ''

ffmpeg_command = 'ffmpeg -i "{}" -f wav -vn "{}"'
whisper_command = 'whispercli  -gpu "NVIDIA GeForce GTX 1050 Ti" -nt -m "C:\\Program Files\\whispercli\\ggml-large.bin" -l zh  -nt -otxt -f "{}"'

# 使用FFmpeg将视频转换为音频
def convert_video_to_audio(video_path, audio_path, video_name):
    ffmpeg_output = subprocess.check_output(
        ffmpeg_command.format(video_path, audio_path),
        shell=True,
        stderr=subprocess.DEVNULL,  # 阻止FFmpeg输出显示在终端上
    )
    
# 使用Whisper将音频转换为文字
def gen_audio_txt(audio_path, video_name):
    # 不指定文件名，自动就是同名的txt
    whisper_output = subprocess.check_output(
        whisper_command.format( audio_path),
        shell=True,
        encoding='utf-8'
    )  

# 这里用来处理视频文件，生成文件
def process_video():
    start_time = time.time()
    # 遍历视频文件目录中的所有视频文件
    n = 0
    video_files = [f for f in os.listdir(video_directory) if f.endswith((".mp4", ".avi", ".mkv", ".flv", ".mov"))]

    for video_file in tqdm(video_files, desc='正在处理视频文件 '):
        # 获取视频文件路径和文件名
        video_path = os.path.join(video_directory, video_file)
        video_name = os.path.splitext(video_file)[0]

        # 定义音频文件路径
        audio_path = os.path.join(video_directory, video_name + '.wav')
        # 定义txt文件路径
        txt_path = os.path.join(video_directory, video_name + '.txt')

        # 检查txt文件是否已存在，如果存在则跳过当前视频文件
        if os.path.exists(txt_path):
            print(f"跳过视频文件 【{video_file}】, 对应的文案txt文件已经存在.")
            continue

        # 使用FFmpeg将视频转换为音频
        convert_video_to_audio(video_path, audio_path, video_name)
        
        # 使用Whisper将音频转换为文字
        gen_audio_txt(audio_path, video_name)
        os.remove(audio_path)
        n = n + 1
    end_time = time.time()
    print("一共 {:d}个视频，共耗时: {:.2f}秒".format(n, end_time - start_time))


if __name__ == '__main__':
    path = ''
    while True:
        path = input("输入包含视频文件的目录: ")
        if os.path.exists(path) :
            break
        else:
            print(f'{path}文件不存在，可能是路径不对')

    video_directory = path

    # 开始处理文件
    process_video()



```
运行效果如下：
![](../../images/2023-06-20-01-24-04.png)
这里会卡挺久，后面就好了，这里现实显卡名字了，就是用显卡了
![](../../images/2023-06-20-01-25-05.png)

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
|  -osrt,    |--output-srt    |[false  ] |输出格式是srt，就是时间轴的那个
|  -owts,    |--output-words  |[false  ] |output script for generating karaoke video
|  -ps,      |--print-special |[false  ] |print special tokens
|  -nc,      |--no-colors     |[false  ] |do not print colors
|  -nt,      |--no-timestamps |[false  ] |不要输出时间轴信息，默认是关闭的，就是一行信息，最前面是时间
|  -l LANG,  |--language LANG |[en     ] |这里指的是输入的音频文件，讲的是啥语音，用的是zh
|  -m FNAME, |--model FNAME   |[models/ggml-base.en.bin] |model path
|  -f FNAME, |--file FNAME    |[       ] |输入的文件名，这里大家可以看到，它是音频文件不是视频问题，所以需要转换

* lang 有时候出来是繁体中文，但是都用的是zh

### 3.4 ffmpeg 一起
同理，ffmpeg也是这样实现的。它的命令更复杂更丰富，这里主要是考虑把mp4文件转换成音频文件
![](../../images/2023-06-20-00-58-51.png)
由于前面用的cli是windows下的，所以这里ffmpeg也是windows下的。
下载地址是官方的
https://ffmpeg.org/download.html
![](../../images/2023-06-20-01-00-50.png)

```
ffmpeg -i "{}" -f wav -vn "{}"
```
这里的 :
-i  表示输入文件名
-f  输出文件格式
-vn  输出文件名，这个说法不准确，不过好理解
更复杂的需求可以进一步去了解，东西还是挺多的

之所以选择命令行方式，一个很大的原因是，最开始选择直接用python的时候，无法使用gpu，尝试几个方案都不行,时不时还报错

# 4、Python包实现（调用openai，失败了）
>考虑用Python直接实现，有几个方面的考虑，
> * 前面2个方案都只能在Windows下运行，受限比较多
> * 要配置路径等多出来的事，不利于部署（目前发现这个问题避免不了）
> * 有个隐形的好处，Python直接弄不用事先下载模型，指定参数它会自己去下载

### 4.1 安装ffmpeg
这次换到mac平台下，日常写文章主要是在mac下，下载地址还是官网地址。
https://www.ffmpeg.org/download.html
下载tar包以后，解压
![](../../images/2023-06-20-10-09-28.png)

就那3个步骤
```
./configurate
make
make install
```

我的电脑上安装了brew，所以直接
``` bash
brew install ffmpeg
```
好处是省去了设置路径之类的工作，依赖包也不用管了，坏处就是有点慢，大概折腾了有半个多小时吧，看起来是下各种依赖包
![](../../images/2023-06-20-10-10-45.png)

好习惯，弄好检查一下，看看版本啥的，确保安全，最好另外起个终端，避免执行环境的问题
```
ffmpeg --help
```

### 4.2 如何在Python中使用ffmpeg转换视频为音频
根据测试的结果，直接 
```
pip install ffmpeg
```
安装的结果不对，所欲有人提议用 ffmpeg-python。


想到用这个方案，是因为纯pyhon调用openai的方法失败了，主要是卡在2个问题上
* 没有调用gpu，使用cpu特别慢
* 一直报错，可能是因为

如何看是否启用了gpu，在windows下很容易从任务管理器里面看，最后会发现特别慢

这里一直报文件不存在，换了几个方法

不用ffmpeg，用ffmepg-python也不行

# 5、异常信息和解决方法



https://github.com/ggerganov/whisper.cpp/releases
