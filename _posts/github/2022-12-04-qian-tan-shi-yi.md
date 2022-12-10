---
layout: post
title: "浅滩拾忆 - github page vscode写博客2022折腾记"
description: "github page 重新出发"
category: "github"
modified: 2022-12-04 22:52
tags: "github jekyll "
---
{% include JB/setup %}


下载vscode

安装了几个插件， paste image


# 目标
* 老的博客模板改下
* 在vscode里面用 markdown语法写
* 图片上传方便
* 有评论jekyll vscode github pagejekyll vscode github pagejekyll vscode github page‘
* 写代码的时候简单一点

# 环境准备
* 下载最新版vscode
* 下载几个插件，jekyll，Markdown Preview Enhanced，paste image

# 2022.12.5尝试
目前对jekyll和github page的理解，可能是，github page是一个发布静态页面的地方。
### 静态的好处是加载方便等，坏处是静态要修改比较麻烦。

所以有人就想出来一个方法，静态页面里面变化的部分是内容，不变的部分是模板，或者说展示框架。
那么jekyll之类的工具就把这个过程给弄成这样：

一个比较纯粹的文本文件内容+各种css样式，各种资源，比如图片之类的，最后生成一系列静态页面。

这个过程中，最终基础的部分，也是最有价值的部分，是那个纯粹的文本文件，写这个文本文件，大家选用的格式是markdown。

但是直接用markdown显示，感觉还不够丰富，所以想在这个上面加上各种东西。
这个过程就是jekeyll来弄的。

至于各种theme啥的，都是为了这个事服务的，jekyll或者类似的工具，又标准化了一套东西。

### 尝试一下，发现无法实用jekyll
很久没有用这个环境了，发现jekyll不能用了。
然后试着安装，发现还是不行

{% highlight bash %}
Building native extensions. This could take a while...
ERROR:  Error installing jekyll:
	ERROR: Failed to build gem native extension.
{% endhighlight  %}

网上说ruby版本可能有影响，查了一下版本
ruby -v 

结果是 2多
ruby 2.6.3p62 (2019-04-16 revision 67580) [universal.x86_64-darwin20]

然后升级

brew install jekyll。发现一直在升级 homebrew，想着先升级ruby，大不了死了

* 终端执行如下指令
\curl -sSL https://get.rvm.io | bash -s stable --ruby

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

 一直报这个错   
然后开始有绿色的字，updatesystem，等了老半天，

Installing requirements for osx.
Updating system.....-


...Failed to update Homebrew, follow instructions at

    https://docs.brew.sh/Common-Issues

.and make sure `brew update` works before continuing.
.
Error running 'requirements_osx_brew_update_system ruby-3.0.0',
please read /Users/xxxxxx/.rvm/log/1670248215_ruby-3.0.0/update_system.log
Requirements installation failed with status: 1.

网上又说
brew update-reset
开始要有点升级的意思了。
% brew update-reset                                                                                                                                                                                                                      
==> Fetching /usr/local/Homebrew...
remote: Enumerating objects: 119341, done.
remote: Counting objects: 100% (11092/11092), done.
remote: Compressing objects: 100% (8/8), done.
Receiving objects:  22% (26358/119341), 15.55 MiB | 49.00 KiB/s

然后再升级ruby
brew install ruby

% brew install ruby                                                                                                                                                                                                                      Richardson@chenybindeMacBook-Pro
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
% sudo gem install jekyll                                                                                                                                                                                                                Richardson@chenybindeMacBook-Pro
Password:
Building native extensions. This could take a while...
ERROR:  Error installing jekyll:
	ERROR: Failed to build gem native extension.

    current directory: /Library/Ruby/Gems/2.6.0/gems/http_parser.rb-0.8.0/ext/ruby_http_parser
/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/bin/ruby -I /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0 -r ./siteconf20221206-4978-td4ybu.rb extconf.rb
creating Makefile


---- 
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

  ---
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

--

类似的操作搞了好多次，最终看起来是可以了

==> Pouring mysql--8.0.31.big_sur.bottle.tar.gz
==> Caveats
We've installed your MySQL database without a root password. To secure it run:
    mysql_secure_installation

MySQL is configured to only allow connections from localhost by default

To connect run:
    mysql -u root

To restart mysql after an upgrade:
  brew services restart mysql
Or, if you don't want/need a background service you can just run:
  /usr/local/opt/mysql/bin/mysqld_safe --datadir=/usr/local/var/mysql
==> Summary
🍺  /usr/local/Cellar/mysql/8.0.31: 315 files, 297.6MB
==> Running `brew cleanup mysql`...
Removing: /usr/local/Cellar/mysql/5.7.22... (317 files, 233.9MB)
==> Caveats
==> mysql
We've installed your MySQL database without a root password. To secure it run:
    mysql_secure_installation

MySQL is configured to only allow connections from localhost by default

To connect run:
    mysql -u root

To restart mysql after an upgrade:
  brew services restart mysql
Or, if you don't want/need a background service you can just run:
  /usr/local/opt/mysql/bin/mysqld_safe --datadir=/usr/local/var/mysql

----

神奇的是，这样折腾下来，ruby -v 还是2的版本，jekyll还是不能安装





* 查看rvm版本
rvm -v
* 查看可安装的ruby版本列表
rvm list known
* 安装指定ruby版本 (eg: 3.0.2)
rvm install ruby-3.0.2
* 查看当前使用ruby版本
which rvm
* 设置默认ruby版本 (eg: 3.0.2)
rvm --default use 3.0.2
* 使用指定ruby版本 (eg: 2.6.3)
rvm use ruby-2.6.3
* 卸载指定ruby版本 (eg: 2.6.3)
rvm remove 2.6.3

---
前面折腾了好久，用这个算是好了？

----

Successfully installed mercenary-0.4.0
Successfully installed liquid-4.0.3
Successfully installed kramdown-2.4.0
Successfully installed kramdown-parser-gfm-1.1.0
Building native extensions. This could take a while...
Successfully installed ffi-1.15.5
Successfully installed rb-inotify-0.10.1
Successfully installed rb-fsevent-0.11.2
Successfully installed listen-3.7.1
Successfully installed jekyll-watch-2.2.1
Building native extensions. This could take a while...
Successfully installed sassc-2.4.0
Successfully installed jekyll-sass-converter-2.2.0
Successfully installed concurrent-ruby-1.1.10
Successfully installed i18n-1.12.0
Building native extensions. This could take a while...
Successfully installed http_parser.rb-0.8.0
Building native extensions. This could take a while...
ERROR:  Error installing jekyll:
	ERROR: Failed to build gem native extension.

    current directory: /Users/Richardson/.rvm/gems/ruby-3.1.3/gems/eventmachine-1.2.7/ext
/Users/Richardson/.rvm/rubies/ruby-3.1.3/bin/ruby -I /Users/Richardson/.rvm/rubies/ruby-3.1.3/lib/ruby/3.1.0 extconf.rb
checking for -lcrypto... yes
checking for -lssl... yes
checking for openssl/ssl.h... yes
checking for openssl/err.h... yes
checking for rb_trap_immediate in ruby.h,rubysig.h... no
checking for rb_thread_blocking_region()... no
checking for rb_thread_call_without_gvl() in ruby/thread.h... yes
checking for rb_thread_fd_select()... yes
checking for rb_fdset_t in ruby/intern.h... yes
checking for rb_wait_for_single_fd()... yes
checking for rb_enable_interrupt()... no
checking for rb_time_new()... yes
checking for inotify_init() in sys/inotify.h... no
checking for __NR_inotify_init in sys/syscall.h... no
checking for writev() in sys/uio.h... yes
checking for pipe2() in unistd.h... no
checking for accept4() in sys/socket.h... no
checking for SOCK_CLOEXEC in sys/socket.h... no
checking for sys/event.h... yes
checking for sys/queue.h... yes
checking for clock_gettime()... yes
checking for CLOCK_MONOTONIC_RAW in time.h... yes
checking for CLOCK_MONOTONIC in time.h... yes
CXXFLAGS=-fdeclspec -Wall -Wextra -Wno-deprecated-declarations -Wno-ignored-qualifiers -Wno-unused-result -Wno-address
creating Makefile

current directory: /Users/Richardson/.rvm/gems/ruby-3.1.3/gems/eventmachine-1.2.7/ext
make DESTDIR\= sitearchdir\=./.gem.20221208-23916-x858zj sitelibdir\=./.gem.20221208-23916-x858zj clean

current directory: /Users/Richardson/.rvm/gems/ruby-3.1.3/gems/eventmachine-1.2.7/ext
make DESTDIR\= sitearchdir\=./.gem.20221208-23916-x858zj sitelibdir\=./.gem.20221208-23916-x858zj
compiling binder.cpp
In file included from binder.cpp:20:
./project.h:119:10: fatal error: 'openssl/ssl.h' file not found
#include <openssl/ssl.h>
         ^~~~~~~~~~~~~~~
1 error generated.
make: *** [binder.o] Error 1

make failed, exit code 2

Gem files will remain installed in /Users/Richardson/.rvm/gems/ruby-3.1.3/gems/eventmachine-1.2.7 for inspection.
Results logged to /Users/Richardson/.rvm/gems/ruby-3.1.3/extensions/x86_64-darwin-20/3.1.0/eventmachine-1.2.7/gem_make.out

看看咋解决

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

--
尴尬了一下，

➜  51xpage.github.com git:(master) git push
Username for 'https://github.com': 51xpage@chenybin.com
Password for 'https://51xpage@chenybin.com@github.com':
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/51xpage/51xpage.github.com/'


--
chenybindeMacBook-Pro :: Dropbox/Study/51xpage.github.com 255 » ssh -T 51xpage@github.com
Warning: Permanently added the RSA host key for IP address '20.205.243.166' to the list of known hosts.
51xpage@github.com: Permission denied (publickey).

---

ssh  51xpage@github.com
提示说是：

调试参数是 

ssh -vT 51xpage@github.com

OpenSSH_8.1p1, LibreSSL 2.7.3
debug1: Reading configuration data /Users/Richardson/.ssh/config
debug1: /Users/Richardson/.ssh/config line 8: Applying options for github.com
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 47: Applying options for *
debug1: Connecting to github.com port 22.
debug1: Connection established.
debug1: identity file /Users/Richardson/.ssh/id_rsa type 0
debug1: identity file /Users/Richardson/.ssh/id_rsa-cert type -1
debug1: Local version string SSH-2.0-OpenSSH_8.1
debug1: Remote protocol version 2.0, remote software version babeld-456f9bbd
debug1: no match: babeld-456f9bbd
debug1: Authenticating to github.com:22 as '51xpage'
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: algorithm: curve25519-sha256
debug1: kex: host key algorithm: rsa-sha2-512
debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: Server host key: ssh-rsa SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8
debug1: Host 'github.com' is known and matches the RSA host key.
debug1: Found key in /Users/Richardson/.ssh/known_hosts:11
debug1: rekey out after 134217728 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: rekey in after 134217728 blocks
debug1: Will attempt key: /Users/Richardson/.ssh/id_rsa RSA SHA256:LofX8qEfxbF5VULFRYkAyApflu0XIzKmMTq+lyLBaYs explicit
debug1: SSH2_MSG_EXT_INFO received
debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519-cert-v01@openssh.com,ecdsa-sha2-nistp521-cert-v01@openssh.com,ecdsa-sha2-nistp384-cert-v01@openssh.com,ecdsa-sha2-nistp256-cert-v01@openssh.com,sk-ssh-ed25519-cert-v01@openssh.com,sk-ecdsa-sha2-nistp256-cert-v01@openssh.com,rsa-sha2-512-cert-v01@openssh.com,rsa-sha2-256-cert-v01@openssh.com,ssh-rsa-cert-v01@openssh.com,sk-ssh-ed25519@openssh.com,sk-ecdsa-sha2-nistp256@openssh.com,ssh-ed25519,ecdsa-sha2-nistp521,ecdsa-sha2-nistp384,ecdsa-sha2-nistp256,rsa-sha2-512,rsa-sha2-256,ssh-rsa>
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey
debug1: Next authentication method: publickey
debug1: Offering public key: /Users/Richardson/.ssh/id_rsa RSA SHA256:LofX8qEfxbF5VULFRYkAyApflu0XIzKmMTq+lyLBaYs explicit
debug1: Authentications that can continue: publickey
debug1: No more authentication methods to try.
51xpage@github.com: Permission denied (publickey).
chenybindeMacBook-Pro :: Dropbox/Study/51xpage.github.com 255 »


从这里可以看出来，它实际上上先去找knows_host，然后再继续，删除了试试？
debug1: Server host key: ecdsa-sha2-nistp256 SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM
The authenticity of host 'github.com (20.205.243.166)' can't be established.
ECDSA key fingerprint is SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com' (ECDSA) to the list of known hosts.
Warning: the ECDSA host key for 'github.com' differs from the key for the IP address '20.205.243.166'
Offending key for IP in /Users/Richardson/.ssh/known_hosts:19
Are you sure you want to continue connecting (yes/no)? yes

--
ssh -T git@github.com

改成这个就可以了，啥情况呀

但是git push还是不行，继续，还是要输入用户名密码

修改一下 .git/config  里面的地址，https改成ssh，
好像还是不行，奇怪了

--
Github permission denied: ssh add agent has no identities

ssh-add ~/.ssh/id_rsa
--
现在的情况是  ssh -T git@github.com 成功，但是git push失败
这里有点细节，ssh -t 会提示认证，git push也会提示
ssh的提示是 
Warning: the ECDSA host key for 'github.com' differs from the key for the IP address '20.205.243.166'
Offending key for IP in /Users/Richardson/.ssh/known_hosts:19
Matching host key in /Users/Richardson/.ssh/known_hosts:20
Are you sure you want to continue connecting (yes/no)? yes

git push的提示是
Warning: the ECDSA host key for 'github.com' differs from the key for the IP address '20.205.243.166'
Offending key for IP in /Users/Richardson/.ssh/known_hosts:19
Matching host key in /Users/Richardson/.ssh/known_hosts:20
不说一毛一样的，也是一毛一样了。

----
最后是这样解决的，
vim .git/config,地址改成  git@github.com:51xpage/51xpage.github.com.git
也就是ssh的地址，好像可以了

---
总算可以提交了，但是有很多内容看起来是不合适？
The kramdown gem before 2.3.0 for Ruby processes the template option inside Kramdown documents by default, which allows unintended read access (such as template="/etc/passwd") or unintended embedded Ruby code execution (such as a string that begins with template="string://<%= `). NOTE: kramdown is used in Jekyll, GitLab Pages, GitHub Pages, and Thredded Forum.

--
   Warning: Highlight Tag no longer supports rendering with Pygments.

``` javascript
alert(11);
```   