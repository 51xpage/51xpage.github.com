---
layout: post
title: "重新出发003——各种重新安装遇到的状况"
description: "github pages 和 jekyll的关系"
category: "github"
modified: 2022-12-14 00:00
tags: "jekyll github pages"

---
* content
{:toc}

#  尝试一下，发现无法实用jekyll
很久没有用这个环境了，发现jekyll不能用了。无法运行
然后试着安装，发现还是不行

``` bash 
Building native extensions. This could take a while...
ERROR:  Error installing jekyll:
	ERROR: Failed to build gem native extension.
```

# 网上说ruby版本可能有影响，查了一下版本
``` bash
ruby -v
``` 

结果版本是 2多
``` bash
ruby 2.6.3p62 (2019-04-16 revision 67580) [universal.x86_64-darwin20]
```
<!-- more -->
# 升级homebrew失败
```
brew install jekyll。
```

发现一直在升级 homebrew，想着先升级ruby，大不了死了

> 终端执行如下指令
``` bash
\curl -sSL https://get.rvm.io | bash -s stable --ruby
```
结果是这样的
``` bash
Unsupported operator '2.5.7'.
/usr/local/Homebrew/Library/Homebrew/version.rb:365:in `initialize': Version value must be a string; got a NilClass () (TypeError)
	from /usr/local/Homebrew/Library/Homebrew/os/mac/version.rb:28:in `initialize'
	from /usr/local/Homebrew/Library/Homebrew/os/mac.rb:18:in `new'
	from /usr/local/Homebrew/Library/Homebrew/os/mac.rb:18:in `version'
	from /usr/local/Homebrew/Library/Homebrew/os/mac.rb:48:in `prerelease?'
	from /usr/local/Homebrew/Library/Homebrew/os.rb:17:in `<module:OS>'
	from /usr/local/Homebrew/Library/Homebrew/os.rb:1:in `<top (required)>'
	from /usr/local/Homebrew/Library/Homebrew/vendor/portable-ruby/2.3.3_2/lib/ruby/2.3.0/rubygems/core_ext/kernel_require.rb:55:in `require'
	from /usr/local/Homebrew/Library/Homebrew/vendor/portable-ruby/2.3.3_2/lib/ruby/2.3.0/rubygems/core_ext/kernel_require.rb:55:in `require'
	from /usr/local/Homebrew/Library/Homebrew/global.rb:91:in `<top (required)>'
	from /usr/local/Homebrew/Library/Homebrew/vendor/portable-ruby/2.3.3_2/lib/ruby/2.3.0/rubygems/core_ext/kernel_require.rb:55:in `require'
	from /usr/local/Homebrew/Library/Homebrew/vendor/portable-ruby/2.3.3_2/lib/ruby/2.3.0/rubygems/core_ext/kernel_require.rb:55:in `require'
	from /usr/local/Homebrew/Library/Homebrew/brew.rb:23:in `<main>'
```


> 一直报这个错   
> 然后开始有绿色的字，updatesystem，等了老半天，

``` bash
Installing requirements for osx.
Updating system.....-


...Failed to update Homebrew, follow instructions at

    https://docs.brew.sh/Common-Issues

.and make sure `brew update` works before continuing.
.
Error running 'requirements_osx_brew_update_system ruby-3.0.0',
please read /Users/xxxxxx/.rvm/log/1670248215_ruby-3.0.0/update_system.log
Requirements installation failed with status: 1.

```

意思是先升级呗

### 网上又说要brew update-reset
开始要有点升级的意思了。
```
% brew update-reset                                                                                 
==> Fetching /usr/local/Homebrew...
remote: Enumerating objects: 119341, done.
remote: Counting objects: 100% (11092/11092), done.
remote: Compressing objects: 100% (8/8), done.
Receiving objects:  22% (26358/119341), 15.55 MiB | 49.00 KiB/s
```


> 然后再升级ruby
```
brew install ruby
#    homebrew-core is a shallow clone


Error:
  homebrew-core is a shallow clone.
To `brew update`, first run:
  git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core fetch --unshallow
This command may take a few minutes to run due to the large size of the repository.
This restriction has been made on GitHub's request because updating shallow
clones is an extremely expensive operation due to the tree layout and traffic of
Homebrew/homebrew-core and Homebrew/homebrew-cask. We don't do this for you
automatically to avoid repeatedly performing an expensive unshallow operation in
CI systems (which should instead be fixed to not use shallow clones). Sorry for
the inconvenience!
Warning: ruby 3.1.2_1 is already installed and up-to-date.
To reinstall 3.1.2_1, run:
  brew reinstall ruby
 ~

```
# 不行换sudo执行看看？
``` bash
% sudo gem install  jekyll                                                             
```   
```  
Building native extensions. This could take a while...
ERROR:  Error installing jekyll:
	ERROR: Failed to build gem native extension.

    current directory: /Library/Ruby/Gems/2.6.0/gems/http_parser.rb-0.8.0/ext/ruby_http_parser
/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/bin/ruby -I /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0 -r ./siteconf20221206-4978-td4ybu.rb extconf.rb
creating Makefile

==> Pouring pkg-config--0.29.2_3.big_sur.bottle.tar.gz
Error: The `brew link` step did not complete successfully
The formula built, but is not symlinked into /usr/local
Could not symlink bin/pkg-config
Target /usr/local/bin/pkg-config
is a symlink belonging to pkg-config. You can unlink it:
  brew unlink pkg-config

To force the link and overwrite all conflicting files:
  brew link --overwrite pkg-config

To list all files that would be deleted:
  brew link --overwrite --dry-run pkg-config

Possible conflicting files are:
/usr/local/bin/pkg-config -> /usr/local/Cellar/pkg-config/0.28/bin/pkg-config
/usr/local/share/aclocal/pkg.m4 -> /usr/local/Cellar/pkg-config/0.28/share/aclocal/pkg.m4
Error: Could not symlink share/doc/pkg-config/pkg-config-guide.html
Target /usr/local/share/doc/pkg-config/pkg-config-guide.html
is a symlink belonging to pkg-config. You can unlink it:
  brew unlink pkg-config

To force the link and overwrite all conflicting files:
  brew link --overwrite pkg-config

To list all files that would be deleted:
  brew link --overwrite --dry-run pkg-config

```

# 基本上不断overwrite，不断重新update，逢山开路，御水修桥
``` bash
  ==> Installing dependencies for mackup: mpdecimal, sqlite, python@3.11 and six
==> Installing mackup dependency: mpdecimal
==> Pouring mpdecimal--2.5.1.big_sur.bottle.tar.gz
🍺  /usr/local/Cellar/mpdecimal/2.5.1: 71 files, 2.1MB
==> Installing mackup dependency: sqlite
==> Pouring sqlite--3.40.0.big_sur.bottle.1.tar.gz
🍺  /usr/local/Cellar/sqlite/3.40.0: 11 files, 4.4MB
==> Installing mackup dependency: python@3.11
==> Pouring python@3.11--3.11.0.big_sur.bottle.tar.gz
Error: An unexpected error occurred during the `brew link` step
The formula built, but is not symlinked into /usr/local
Permission denied @ dir_s_mkdir - /usr/local/Frameworks
Error: Permission denied @ dir_s_mkdir - /usr/local/Frameworks

```

> 神奇的是，这样折腾下来，ruby -v 还是2的版本，jekyll还是不能安装


```
Successfully installed mercenary-0.4.0
Successfully installed liquid-4.0.3
Successfully installed kramdown-2.4.0
Successfully installed kramdown-parser-gfm-1.1.0
Building native extensions. This could take a while...
Successfully installed ffi-1.15.5
Successfully installed rb-inotify-0.10.1
Successfully installed rb-fsevent-0.11.2
./project.h:119:10: fatal error: 'openssl/ssl.h' file not found
#include <openssl/ssl.h>
         ^~~~~~~~~~~~~~~
1 error generated.
make: *** [binder.o] Error 1

make failed, exit code 2

Gem files will remain installed in /Users/Richardson/.rvm/gems/ruby-3.1.3/gems/eventmachine-1.2.7 for inspection.
Results logged to /Users/Richardson/.rvm/gems/ruby-3.1.3/extensions/x86_64-darwin-20/3.1.0/eventmachine-1.2.7/gem_make.out
```
> openssl ,看起来是要重新设置一下路径
看看咋解决
``` 
gem install eventmachine -- --with-cppflags=-I/usr/local/opt/openssl/include  

gem install jekyll总算是好了

  ~ gem install eventmachine -- --with-cppflags=-I/usr/local/opt/openssl/include
Building native extensions with: '--with-cppflags=-I/usr/local/opt/openssl/include'
This could take a while...
Successfully installed eventmachine-1.2.7
Parsing documentation for eventmachine-1.2.7
Installing ri documentation for eventmachine-1.2.7
Done installing documentation for eventmachine after 28 seconds
1 gem installed
➜  ~ gem install jekyll
Successfully installed em-websocket-0.5.3
Successfully installed colorator-1.1.0
Successfully installed public_suffix-5.0.1
Successfully installed addressable-2.8.1
Successfully installed jekyll-4.3.1
Parsing documentation for em-websocket-0.5.3
Installing ri documentation for em-websocket-0.5.3
Parsing documentation for colorator-1.1.0
Installing ri documentation for colorator-1.1.0
Parsing documentation for public_suffix-5.0.1
Installing ri documentation for public_suffix-5.0.1
Parsing documentation for addressable-2.8.1
Installing ri documentation for addressable-2.8.1
Parsing documentation for jekyll-4.3.1
Installing ri documentation for jekyll-4.3.1
Done installing documentation for em-websocket, colorator, public_suffix, addressable, jekyll after 2 seconds
5 gems installed
```

尴尬了一下，