# 登录 {#登录}

* 再上一遍流程图，接下来的代码就按照这个逻辑来写

![](images/login.png "登录流程")

* 创建user\_login.py文件，代码如下

```py
#coding=utf-8
from MySQLdb import *
from hashlib import sha1

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
        sql='select upwd from py_users where uname=%s'
        params=[uname]
        conn=connect(host='localhost',port=3306,database='python',user='root',password='mysql',charset='utf8')
        cur=conn.cursor()
        cur.execute(sql,params)
        result=cur.fetchone()
        if result==None:
            print '用户名错误，登录失败'
        elif result[0]==upwd_sha1:
            print '登录成功'
        else:
            print '密码错误，登录失败'
        cur.close()
    except Exception,e:
        print '登录失败，错误原因：%s'%e
    finally:
        conn.close()
```



