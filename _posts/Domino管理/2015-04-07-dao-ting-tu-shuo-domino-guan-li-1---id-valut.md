---
layout: single
title: "道听途说Domino管理1 - ID Valut"
description: "domino的ID文件管理"
category: "Domino管理"
modified: 2015-04-07 15:04
tags: "Domino管理 ID Vault"
---
{% include JB/setup %}
## ID文件
   Domino的安全体系一直为人们所称道，保证了整个Domino经久不衰。它很好的平衡了易用性和安全。  
    做为安全体系的重要组成部分，ID文件，用于标识Domino中的安全基础元素。   
    从上到下的管理大致可以分为：   
    
   * 组织（O）
   * 组织单元(OU)
   * 服务器(Server)
   * 个人(User)
    
   传统的C/S模式应用中，ID文件扮演着重要的角色，所以的数据传输都会经过ID文件加解密。Domino提供一个证书的发放中心，为每个安全实体发放ID文件。并提供验证服务。  
    就最基础的验证而言，它提供了密码的验证方式，但是这个密码是基于id文件的。如果id文件丢失，将无法访问Domino的资源。
    很长一段时间内，id文件的丢失是非常严重而无奈的事情，基本上只能重新注册。而某些用ID密钥加密的信息也将永远无法解开了。

   当然，这种相对封闭的安全体系在B/S下几乎丧失殆尽了。
    
## ID Vault
   正是因为ID文件的重要性，和丢失ID文件带来的巨大不变。所以很多运维人员为了避免因为ID文件丢失或者损坏引起的麻烦。会在用户注册之初留下id文件的备份。
    通常这种做法无法解决几个问题：
    
   1. 用户id更新无法联动，如密码调整
   2. 通常还需要修改个人文档。
    
   所以在Domino 8的时候引入了ID Valut功能。即ID保险箱的功能。  
   ID Valut的启用是比较简单的。本质上就是将用户的ID文件统一保存在一个数据库中。通过保险箱数据库的ACL来保障id文件安全。  
    当然，仅仅服务器做改变是不够的。当用户的id文件更新时，就需要借助客户端的功能。而且当用户需要修改密码等操作时，也会涉及信息的变更。  
    所以客户端的密码修改就会牵涉到保险箱中文件的更新。

## 自助重置
   Domino提供了一系列的API来处理ID Valut相关功能。使得
  
   * Web密码和ID密码一致变得简单
   * Web上重置ID密码变得可能
   
   实际上这些API提供了很大的权限，未经用户许可就能修改用户id密码。
   这给管理员提供了很大的便利。
    
## 代码示例
   Http密码重置  
   `Call docUser.replaceItemValue("HTTPPassword", 新密码)`
   Notes密码重置  
   `Call notesSession.ResetUserPassword( IdVault服务器, 用户名, 新密码 )`    


## 更新
几个api和示例  
domino的安全机制
完整的流程图

===
