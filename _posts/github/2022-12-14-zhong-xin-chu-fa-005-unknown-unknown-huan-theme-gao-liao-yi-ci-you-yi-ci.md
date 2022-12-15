---
layout: post
title: "重新出发005——换theme搞了一次又一次"
description: "jekyll的theme是咋回事，好复杂"
category: "github"
modified: 2022-12-14 08:52
tags: "jekyll github pages"

---
* content
{:toc}

## 主题和皮肤什么鬼



太窄了

没有目录
toc: true



开始换皮肤
--- 
``` bash
rake theme:install git="https://github.com/pages-themes/hacker.git"

Cloning into './_theme_packages/_tmp'...
remote: Enumerating objects: 444, done.
remote: Total 444 (delta 0), reused 0 (delta 0), pack-reused 444
Receiving objects: 100% (444/444), 105.06 KiB | 703.00 KiB/s, done.
Resolving deltas: 100% (208/208), done.
rake aborted!
Errno::ENOENT: No such file or directory @ rb_sysopen - ./_theme_packages/_tmp/manifest.yml
/Users/Richardson/Dropbox/Study/51xpage.github.com/Rakefile:348:in `initialize'
/Users/Richardson/Dropbox/Study/51xpage.github.com/Rakefile:348:in `open'
/Users/Richardson/Dropbox/Study/51xpage.github.com/Rakefile:348:in `verify_manifest'
/Users/Richardson/Dropbox/Study/51xpage.github.com/Rakefile:329:in `theme_from_git_url'
/Users/Richardson/Dropbox/Study/51xpage.github.com/Rakefile:230:in `block (2 levels) in <top (required)>'
```
但是比较遗憾，还是出错了，继续呗。

好像是这个东西本身的问题，换了其他的主题好像可以，但是不喜欢其他的，换一下

---
rake theme:install
rake theme:

初步可以判定，这个玩意不是同一个东西，文件夹结构差别很大，jekyllbootstrap 这个系列下面的内容，大多数都在2010年前后，说明这个玩意已经不行了，所以说啥都得换了。


手工建个Gemfile可以吗
---

``` bash
(master)⚡ [15] % vim Gemfile                                                                                                                                                                                                          ~/Dropbox/Study/51xpage.github.com
(master)⚡ % bundle                                                                                                                                                                                                                    ~/Dropbox/Study/51xpage.github.com
Fetching gem metadata from https://rubygems.org/...........
Resolving dependencies........
Using bundler 2.3.26
Using concurrent-ruby 1.1.10
Using colorator 1.1.0
Fetching commonmarker 0.23.6
Fetching execjs 2.8.1
Fetching minitest 5.16.3
Fetching thread_safe 0.3.6
Fetching public_suffix 4.0.7
Fetching unf_ext 0.0.8.2
Fetching zeitwerk 2.6.6
Fetching coffee-script-source 1.11.1
Installing zeitwerk 2.6.6
Using eventmachine 1.2.7
Using http_parser.rb 0.8.0

^ 


```

---
---

@、
 import '/jekyll-theme-hacker';
---


--
折腾一圈下来好像没啥用，本地看起来，少css，
无意中发现 _layout文件夹里面的文件有点问题。

``` yaml
---
layout: default
---
{- % include JB/setup % }
{-  % include themes/hsptr/_config.yml % }
```

类似这样的，于是把它改成hacker看看

``` bash
jekyll 3.9.2 | Error:  Could not locate the included file 'themes/hacker/post.html' in any of ["51xpage.github.com/_includes", "/private/var/folders/pl/y4d2fmrx15db3j2f12nc84sm0000gn/T/jekyll-remote-theme-20221211-6424-qscgui/_includes"]. Ensure it exists in one of those directories and is not a symlink as those are not allowed in safe mode.
/.rvm/gems/ruby-3.1.3/gems/jekyll-3.9.2/lib/jekyll/tags/include.rb:121:in `locate_include_file': Could not locate the included file 'themes/hacker/post.html' in any of ["/51xpage.github.com/_includes", "/private/var/folders/pl/y4d2fmrx15db3j2f12nc84sm0000gn/T/jekyll-remote-theme-20221211-6424-qscgui/_includes"]. Ensure it exists in one of those directories and is not a symlink as those are not allowed in safe mode. (IOError)
	from /Users/Richardson/.rvm/gems/ruby-3.1.3/gems/jekyll-3.9.2/lib/jekyll/tags/include.rb:130:in `render'

```  

目前看起来，原理大概是是说，有个地方放theme，真正起作用的东西都在根目录，也就是
_posts.  _layouts等文件夹。
换句话来说，这些界面风格，并没有包含分页之类的东西，那些东西还得自己折腾。


安装admin
--

在Gemfile中加入

``` bash
gem 'jekyll-admin', group: :jekyll_plugins
···

``` bash



bundle install

Using jekyll-theme-tactile 0.2.0
Using github-pages 227
Installing mustermann 3.0.0
Installing multi_json 1.15.0
Installing rack 2.2.4
Fetching rack-protection 3.0.4
Installing tilt 2.0.11
Installing rack-protection 3.0.4
Fetching sinatra 3.0.4

Retrying download gem from https://rubygems.org/ due to error (2/4): Gem::RemoteFetcher::FetchError Net::OpenTimeout: Failed to open TCP connection to rubygems.org:443 (execution expired) (https://rubygems.org/gems/sinatra-3.0.4.gem)
Installing sinatra 3.0.4
Fetching sinatra-contrib 3.0.4
Installing sinatra-contrib 3.0.4
Fetching jekyll-admin 0.11.1
Installing jekyll-admin 0.11.1
Bundle complete! 4 Gemfile dependencies, 101 gems now installed.
Use `bundle info [gemname]` to see where a bundled gem is installed.

```

在./config.yml中加入

``` yaml
jekyll_admin:
  hidden_links:
    - posts
    - pages
    - staticfiles
    - datafiles
    - configuration
  homepage: "pages"



```  


改了Gemfile，另外加了default.html,修改了sysle.scss文件，暂时看起来是好了

----

但是还是离我的目标有点距离。hacker的文章风格是我期望的，导航条不好，可能是因为我的配置有问题。
这个过程中，大概发现了一些东西，_layouts这个文件夹应该是比较重要的文件夹，文章是从_posts里面，经过_layouts包装，到达_site文件夹。这个_layouts会用到 _includes和 assets等内容。
jekyll的教程好像也是这么说的。

Minimal Mistakes
---
官方的说法是加个theme就好了，实际操作好像不是这样，可能是因为原来的文件夹