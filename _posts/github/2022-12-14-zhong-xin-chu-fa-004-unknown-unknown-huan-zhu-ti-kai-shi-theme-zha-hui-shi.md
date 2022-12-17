---
layout: post
title: "重新出发004——github上不去，ssh也不行"
description: "github pages 和 jekyll的关系"
category: "github"
modified: 2022-12-14 00:01
tags: "jekyll github pages"
---
* content
{:toc}

# 新问题不能提交到github了

  {% highlight bash %}  
➜  51xpage.github.com git:(master) git push
Username for 'https://github.com': 51xpage@chenybin.com
Password for 'https://51xpage@chenybin.com@github.com':
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/51xpage/51xpage.github.com/'

{% endhighlight %}  

--
>意思就是2021以后不能用密码了呗，要用key了呗

# 赶紧去弄个key去，测试一下

```
ssh -T 51xpage@github.com
Warning: Permanently added the RSA host key for IP address '20.205.243.166' to the list of known hosts.
51xpage@github.com: Permission denied (publickey).
```
<!-- more -->
# 学个新技能，看看ssh是咋弄的，多个v

> 看起来是会在 **knows_host** 里面留下点啥

  {% highlight bash %}  
ssh -vT 51xpage@github.com
OpenSSH_8.1p1, LibreSSL 2.7.3
debug1: Reading configuration data /Users/Richardson/.ssh/config
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 47: Applying options for *
debug1: Server host key: ssh-rsa SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8
debug1: Host 'github.com' is known and matches the RSA host key.
debug1: rekey out after 134217728 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: rekey in after 134217728 
debug1: SSH2_MSG_EXT_INFO received
debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519-cert-v01@openssh.com,  
{% endhighlight %}  

# 它实际上上先去找knows_host，然后再继续，删除了试试？
``` bash
debug1: Server host key: ecdsa-sha2-nistp256 SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM
The authenticity of host 'github.com (20.205.243.166)' can't be established.
ECDSA key fingerprint is SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com' (ECDSA) to the list of known hosts.
Warning: the ECDSA host key for 'github.com' differs from the key for the IP address '20.205.243.166'
Offending key for IP in /Users/Richardson/.ssh/known_hosts:19
Are you sure you want to continue connecting (yes/no)? yes
```

# 统一是 git@github.com
``` bash
ssh -T git@github.com
```

改成这个就可以了，啥情况呀

# 还是不行

但是git push还是不行，继续，还是要输入用户名密码

修改一下 .git/config  里面的地址，https改成ssh，
好像还是不行，奇怪了


> Github permission denied: ssh add agent has no identities

试试看

``` bash
ssh-add ~/.ssh/id_rsa
```

# 总结一下失败状况
现在的情况是  ssh -T git@github.com 成功，但是git push失败
这里有点细节，ssh -t 会提示认证，git push也会提示
ssh的提示是 
```
Warning: the ECDSA host key for 'github.com' differs from the key for the IP address 
Are you sure you want to continue connecting (yes/no)? yes

git push的提示是
Warning: the ECDSA host key for 'github.com' differs from the key for the IP address 
```
不说一毛一样的，也是一毛一样了。

# 最后居然是这样解决的

vim .git/config,
地址改成  git@github.com:51xpage/51xpage.github.com.git
也就是ssh的地址，好像可以了，这个地址是从网页上拷贝下来的


总算可以提交了，但是有很多内容看起来是不合适？

> The kramdown gem before 2.3.0 for Ruby processes the template option inside Kramdown documents by default, which allows unintended read access (such as template="/etc/passwd") or unintended embedded Ruby code execution (such as a string that begins with template="string://<%= `). NOTE: kramdown is used in Jekyll, GitLab Pages, GitHub Pages, and Thredded Forum.
   Warning: Highlight Tag no longer supports rendering with Pygments.
