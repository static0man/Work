#!/usr/bin/python
# coding=utf-8
import sys
from redis.sentinel import Sentinel
import time

sentinel = Sentinel([('10.5.5.194', 26379),
                     ('10.5.5.155', 26379),
                     ('10.5.5.128', 26379), ], socket_timeout=0.5)

name = sys.argv[2]

master = sentinel.master_for('mymaster', socket_timeout=0.5, password='root123', db=0)

slave = sentinel.slave_for('mymaster', socket_timeout=0.5, password='root123', db=0)
# 判断是否所传参数对应的value值是否为1
while True:
    time.sleep(1)
    if slave.get(name) == "0" or slave.get(name) is None:
        continue
    else:
        break
master.set(name, "0")
f_do = sys.argv[1] + '.do'
f_dat = sys.argv[1] + '.dat'
f = open(f_dat,'w')
f.write('0'+'\n')
f.write('success'+'\n')
f.write('set '+name+'为0 \n')
f.close()
f = open(f_do,'w')
f.write('')
f.close()