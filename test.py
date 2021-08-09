#coding=utf-8
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# name= 'lili'
# age= 20
# print('my name is {1},age is {0},{0}{1}{1}'.format(name,age))
#
#


#
# try:
#     usrname = str(input("请输入用户名:"))
#     password = int(input("请输入密码:"))
#     if usrname =="zhangjinwei" and password == "123456":
#         print("登录成功")
#     else:
#         print("请输入正确的账号或密码")
# except:
#     print('输入格式不正确')
# finally:
#     print("你可以访问首页浏览")
# print(dir())
import os
# os.mkdir("dsl_project")
# print(os.removedirs("dsl_project"))
import time

print(time.asctime())
print(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# time.strftime()
now_timestamp=time.time()

two_time_after=now_timestamp-60*60*24*2
print(time.localtime())
time_tuple=time.localtime(two_time_after)

print("两天前得时间:",two_time_after)
print(time.strftime("%Y%m%d %H:%M:%S",time_tuple))
print(time.strftime("%Y{y}%m{m}%d{d} %H{h}:%M{M}:%S{S}").format(y="年",m="月",d="日",h="时",M="分",S="秒"))






