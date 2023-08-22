---
layout: post
title: "重新出发006——迁移图片到文件名对应文件件"
description: "迁移图片文件到对应文件夹"
category: "github"
modified: 2023-08-23 01:20
tags: "python jeklly images"
---
* content
{:toc}

> 最近因为学习的原因用了hexo，触动比较大的主要是图片的处理，原来实用jekyll的时候，图片都是放在统一的images文件夹下，可想而知，时间超长一点就很痛苦了。今天记录一下图片迁移的过程，
<!-- more -->
# 1、问题由来-图片太乱
hexo有一个拼音插件，可以把中文的文件名路径转换成拼音，而Jeklly暂时还没有找到对应的插件，目前还是实用最原始的ruby脚本自动生成。

> 简单来说，jekyll现在的解决方案，在提交到git之前就生成好了拼音路径。而hexo的插件是提交之后自己生成的，对我来说无感觉。

目前考虑分2步走，第一步先把图片文件放到文件路径里面去，第二步找个图床方案吧。

# 2、实现思路
插播一句，pycharm破解失效了，就尝试用了Jupyter，真香！

![](../../images/2023-08-23-zhong-xin-chu-fa-006-unknown-unknown-qian-yi-tu-pian-dao-wen-jian-ming-dui-ying-wen-jian-jian/2023-08-23-01-28-00.png)

选中部分单独执行，调试起来太方便了，只选中部分运行，如果临时需要弄个测试函数的代码，随便搞一段。完全不用考虑重新弄个命令行还是啥的就运行了，太爽了！

* 目的是为了遍历所有_post下面的文件夹，找到里面的文件
* 逐行便利，如果发现里面有![](../../images/  这个开头的内容，然后后面没有斜杠了（它是用来判断我们是否处理过）
* 我们就去../../images下面创建一个同名的目录，当然先判断它是否存在。
* 然后把这个内容后面的文件名，也就是)前面的内容，这个文件移动到这里去
* 修改这个文件
* 如果文件不是很多，最后的判断方式就是看images下面还有孤立文件吗？如果没有就通过sourcetree看一下，文件内容有修改的，看一下是否正常显示

# 3、代码实现

``` python
import os
import shutil

# 移动图片文件
def move_image_file(image_file, images_path, mdpath):
    print(f'image_file:{image_file}, images_path:{images_path}, mdpath:{mdpath}')
    # 创建文件夹
    if not os.path.exists(images_path + mdpath):
        os.makedirs(images_path + mdpath)
        
    # 安全起见，还是复制吧
    if not os.path.exists(images_path + mdpath + "/" + image_file):
        shutil.copyfile(images_path + "/" + image_file, images_path + mdpath + "/" + image_file)
    
    return (f'![](../../images/{mdpath}/{image_file})')

# 遍历文件夹
def search_file(path):
    # 如果是目录，递归调用
    for root, ds, fs in os.walk(path):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname

# 读取文件内容
def process_mdfile(filename):
    # 逐行读取，如果需要修改就修改
    # ![](../../images/ 以这个开头
    # 以) 结尾，而且中间没有 / 了
    # 返回的时候修改文件内容并保存
    is_rewrite = False
    new_data = ""
    with open(filename, "r") as f:
        for line in f:
            nPos = line.find('![](../../images/')
            if (nPos != -1):
                print(f'准备开始处理文件：{filename}')
                print(f'修改前{line}')
                line = process_image_file(filename, line)
                is_rewrite = True
                print(f'修改后{line}')
            new_data += line
                
    if(is_rewrite):
        with open(filename, "w") as f:
            f.write(new_data)
        
    return

# 处理图片文件
def process_image_file(filename, image_text):
    # 传入原始的md文件，和图片文件名
    # 创建文件夹，移动文件
    # 注意一行多文件的情况，如 ![](../../images/2023-06-23-00-41-51.png)![](../../images/2023-06-23-00-42-28.png)
    # 返回修改后的内容
    new_text = ""
    mdpath = os.path.basename(filename).replace(".md", "")
    images_path = os.path.dirname(filename).split('_posts')[0] + "images/"
    test_str = '![](../../images/'
    len_test_str = len('![](../../images/')
    nPos_Image = image_text.find(test_str)
    
    new_text = image_text[0 : nPos_Image]
    print(f'nPos_Image:{nPos_Image}, new_text:{new_text}')
    image_text = image_text[nPos_Image + len_test_str : len(image_text)-nPos_Image]
    print(f'image_text:{image_text}')
    while nPos_Image != -1:
        image_file = image_text.split(')')[0]
        nPos_C = image_text.find(")")
        print(image_file)
        # 这里判断一下，如果) 前面还有斜杠，说明处理过了，跳过去
        if image_file.find('/') != -1:
            # 表示处理过了，
            new_text += image_file + ")"
            image_text = image_text[nPos_C - 1: len(image_text)-nPos_C]
        else:
            new_text += move_image_file(image_file, images_path, mdpath)
            image_text = image_text[nPos_C - 1: len(image_text)-nPos_C]
        
        
        nPos_Image = image_text.find(test_str)
            
    
    return new_text

def main():
    while True:
        base = input("请输入jekyll下面的_posts文件夹 ")
        if os.path.exists(base):
            break
        else:
            print(f'{base}路径不存在')

    for file in search_file(base):
        if file.endswith('.md'):
            process_mdfile(file)

if __name__ == '__main__':
    main()

```
# 4、测试坚持
检查的方案也很简单，images根目录的文件，和里面的文件如果重合的，删除掉，没剩就好了
另外本地启动
``` bash
 jeklly server
```
图片都有了就好了

# 4、补充说明