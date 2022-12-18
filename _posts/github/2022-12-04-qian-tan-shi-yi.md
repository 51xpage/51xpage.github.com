---
layout: post
title: "浅滩拾忆 - github page vscode写博客2022折腾记"
description: "github page 重新出发"
category: "github"
modified: 2022-12-04 22:52
tags: "github jekyll "
---
* content
{:toc}

# 问题排查和记录
* 日常写作记录
* 提交到github也没报错，但是页面没更新
* web管理文件，弄个admin
* 咋弄个摘要
* 咋弄个头像
* 表格咋弄
* 图片咋上传
* 搜索
* 访问统计

<!-- more -->

# 1.日常写作格式技巧记录

### 代码格式

Delphi用的是 pascal。
https://jekyll.one/pages/public/previewer/rouge/#void


### 表格


# 2.本地编译好的，但是提交以后没更新
如果有错误，提交的时候会提示，如果没有提示看看邮件。看起来是没有。

这个时候深入一点可以去仓库的Actions里面看一下，是哪个步骤出错了。
![](../../images/2022-12-15-16-50-13.png)

从这里也能更清楚知道jekyll的执行过程

# 3.安装admin
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

# 4.摘要，其实就是截断一下
摘要是通过yaml里面的参数来控制的
```yaml
excerpt_separator: "<!-- more -->"
#excerpt_separator: "\n\n"
```
开始以为是有啥特别的东西，自动计算摘要，发现没起效。
后来才理解它其实是截断，所以现在用了一个明显的标记，而不是4个回车。

# 5.图片和头像
图片得益于微软的收购，现在依稀记得10年前，github的免费仓库有空间限制，所以图片需要借助图床，折腾一段时间没搞定，就没继续了。当时有一些国内空间的软文，但是也是比较折腾的。最后放弃了

# 6. 加搜索
有一个简单的组件可以做这个事，但是展示效果不太好。
https://github.com/christian-fei/Simple-Jekyll-Search

* 下载search.json和simple-jekyll-search.js
分别放在assets和assets/js下

* 修改_includes下面的head.html，增加

``` html
<li>
    <input type="text" id="search-input" placeholder="搜了点啥呢..">
    <ul id="results-container"></ul>
</li>
```

* 修改_includes下面的header.html，增加

``` html
<style>
   #search-demo-container {
        max-width: 40em;
        padding: 1em;
        margin: 1em auto;
        border: 1px solid lightgrey;
      }
  #search-input {
    display: inline-block;
    padding: .5em;
    width: 100%;
    font-size: 0.8em;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
  }
</style>
```

* 修改_layouts下面的 index.html,增加

``` html
<script src="{{ site.baseurl }}/assets/js/simple-jekyll-search.min.js"></script>

<script>
  window.simpleJekyllSearch = new SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    json: '{{ site.baseurl }}/assets/search.json',
    searchResultTemplate: '<li><a href="{url}?query={query}" title="{desc}">{title}</a></li>',
    noResultsText: 'No results found',
    limit: 10,
    fuzzy: false,
    exclude: ['Welcome']
  })
</script>
```
