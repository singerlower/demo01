# MySQL数据表设计 {#实例：用户登录注册}

* 设计用户表py\_users结构如下
  * id
  * uname
  * upwd
  * is\_delete
* 注意：密码要进行加密，绝对不能在数据库中存储明文的密码
* 如果使用md5加密，则密码包含32个字符
* 如果使用sha1加密，则密码包含40个字符
* 这里选择使用sha1加密
* 根据结构创建表的脚本如下

```
create table py_users(
id int unsigned auto_increment not null primary key,
uname varchar(20) not null,
upwd char(40) not null,
is_delete bit not null default 0
);
```



