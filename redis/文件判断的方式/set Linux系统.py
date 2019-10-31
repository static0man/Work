#!/usr/bin/python
# coding=utf-8
import sys
from redis.sentinel import Sentinel
import os

# # 连接哨兵服务器(主机名也可以用域名)
# sentinel = Sentinel([('10.5.5.194', 26379),
#                      ('10.5.5.155', 26379),
#                      ('10.5.5.128', 26379), ], socket_timeout=0.5)
# # # 获取主服务器地址
# # master = sentinel.discover_master('mymaster')
# # print(master)
# # # # 输出：('172.31.0.2', 5001)
# #
# # # # 获取从服务器地址
# # slave = sentinel.discover_slaves('mymaster')
# # print(slave)
# # # # 输出：[('172.31.3', 5001), ('172.31.0.4', 5001), ('172.31.0.5', 5001)]
# #
# # # # 获取主服务器进行写入
# # master = sentinel.master_for('mymaster', socket_timeout=0.5, password='root123', db=0)
# # w_ret = master.set('name', 'myredis is redis')
# # # 输出：True
#
# name = sys.argv[1]
# # # 获取从服务器进行读取
# slave = sentinel.slave_for('mymaster', socket_timeout=0.5, password='root123', db=0)
#
# # 判断是否所传参数对应的value值是否为空或者1，如果是设置为0
# if slave.get(name) is None or slave.get(name) == "0":
#     master.set(name, "1")

name = sys.argv[1]
filePath = '/home/autouser/files_temp'
if os.path.exists(filePath):
    os.system("cd files_temp")
    os.system("touch files_temp/" + name + ".txt")
else:
    os.system("mkdir ~/files_temp/")
    os.system("touch files_temp/" + name + ".txt")
        
f_do = sys.argv[1] + '.do'
f_dat = sys.argv[1] + '.dat'
f = open(f_dat, 'w')
f.write('0'+'\n')
f.write('success'+'\n')
f.write('set '+name+'为1 \n')
f.close()
f = open(f_do, 'w')
f.write('')
f.close()
