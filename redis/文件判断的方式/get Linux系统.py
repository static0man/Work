#!/usr/bin/python
# coding=utf-8

# from redis.sentinel import Sentinel
# # 连接哨兵服务器(主机名也可以用域名)
# sentinel = Sentinel([('10.5.5.194', 26379),
#                      ('10.5.5.155', 26379),
#                      ('10.5.5.128', 26379), ], socket_timeout=0.5)
# # # 获取主服务器地址
# # master = sentinel.discover_master('mymaster')
# # print(master)
# # # 输出：('172.31.0.2', 5001)
# # # 获取从服务器地址
# # slave = sentinel.discover_slaves('mymaster')
# # print(slave)
# # # 输出：[('172.31.3', 5001), ('172.31.0.4', 5001), ('172.31.0.5', 5001)]
# # # 获取主服务器进行写入
# # master = sentinel.master_for('mymaster', socket_timeout=0.5, password='root123', db=0)
# # w_ret = master.set('name', 'myredis is redis')
# # # 输出：True
#
#
# # # 获取从服务器进行读取
# slave = sentinel.slave_for('mymaster', socket_timeout=0.5, password='root123', db=0)
# 判断是否所传参数对应的value值是否为1

import sys
import os
import time

name = sys.argv[1]
filePath = '/home/autouser/files_temp'
# 设置时间间隔读取文件夹
while True:
    time.sleep(5)
    # 获取文件夹里面的文件名称list
    file_lists = os.listdir(filePath)
    file_name = name + ".txt"
    print("111111111111")
    # 判断所传参数对应的文件在不在list里面，存在设置为0
    if file_name in file_lists:
        # 设置完删除对应文件
        f_do = sys.argv[1] + '.do'
        f_dat = sys.argv[1] + '.dat'
        f = open(f_dat, 'w')
        f.write('0' + '\n')
        f.write('success' + '\n')
        f.write('set ' + name + '为1 \n')
        f.close()
        f = open(f_do, 'w')
        f.write('')
        f.close()

        os.system("rm files_temp/" + name + ".txt")

    else:
        f_do = sys.argv[1] + '.do'
        f_dat = sys.argv[1] + '.dat'
        f = open(f_dat, 'w')
        f.write('1' + '\n')
        f.write('false' + '\n')
        f.close()
        f = open(f_do, 'w')
        f.write('')
        f.close()

