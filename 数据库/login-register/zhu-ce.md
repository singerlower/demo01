# 注册 {#mysql数据表设计}

* 再上一遍流程图，接下来的代码就按照这个逻辑来写

![](images/reg.png "注册流程")

* 创建user\_reg.py文件，代码如下

```py
#coding=utf-8

from MySQLdb import *
from hashlib import sha1

if __name__=='__main__':
    try:
        #接收用户输入
        uname=raw_input('请输入用户名：')
        upwd=raw_input('请输入密码：')

        #对密码加密
        s1=sha1()
        s1.update(upwd)
        upwd_sha1=s1.hexdigest()

        #打开与数据库的连接
        conn=connect(host='localhost',port=3306,database='python',user='root',password='mysql',charset='utf8')
        cur=conn.cursor()

        #判断用户名是否存在
        sql='select count(*) from py_users where uname=%s'
        params=[uname]
        cur.execute(sql,params)
        result=cur.fetchone()
        if result[0]==1:
            print '用户名已经存在，注册失败'
        else:
            #用户名不存在
            sql='insert into py_users(uname,upwd) values(%s,%s)'
            params=[uname,upwd_sha1]
            result=cur.execute(sql,params)
            conn.commit()
            if result==1:
                print '注册成功'
            else:
                print '注册失败'
        cur.close()
    except Exception,e:
        print '注册失败，原因是：%s'%e
    finally:
        conn.close()
```



