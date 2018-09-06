# 加入Redis {#加入redis}

* 加入redis后登录逻辑如下图，将图中nosql的位置换为redis即可

![](images/login_redis.png "加入redis后登录流程")

* 用户数据存的键为用户名，值为密码

* 将原来MySQL操作的代码封装到一个方法中，代码如下

```py
def mysql_login():
    #redis中没有则到mysql中查询
    sql='select upwd from py_users where uname=%s'
    params=[uname]
    try:
        conn= connect(host='localhost',port=3306,database='python',user='root',password='mysql',charset='utf8')
        cur=conn.cursor()
        cur.execute(sql,params)
        result=cur.fetchone()
        cur.close()
        if result==None:
            print '用户名错误，登录失败，数据来源于mysql'
        else:
            #当查询到用户及对应的密码时，将数据加入到redis中，以供后续登录使用
            r.set(uname,upwd_sha1)
            #判断密码是否正确
            if result[0]==upwd_sha1:
                print '登录成功，数据来源于mysql'
            else:
                print '密码错误，登录失败，数据来源于mysql'
    except Exception,e:
        print '登录失败，错误原因：%s' % e
    finally:
        conn.close()
```

* 创建user\_redis.py文件，代码如下

```py
#coding=utf-8
from MySQLdb import *
from hashlib import sha1
from redis import *

if __name__=='__main__':
    try:
        #接收输入用户名、密码
        uname=raw_input('请输入用户名：')
        upwd=raw_input('请输入密码：')

        #对密码加密
        s1=sha1()
        s1.update(upwd)
        upwd_sha1=s1.hexdigest()

        #根据用户名查询密码
        #先到redis上查，没有再到mysql上查
        r=StrictRedis()
        result=r.get(uname)
        if result==None:
            mysql_login()
        else:
            #redis中找到了这个用户名的数据
            if result==upwd_sha1:
                print '登录成功，数据来源于redis'
            else:
                print '密码错误，登录失败，数据来源于redis'
    except Exception,e:
        print '登录失败，错误原因：%s'%e
```



