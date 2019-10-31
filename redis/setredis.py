#!/usr/bin/python
# coding=utf-8
import sys
from redis.sentinel import Sentinel

sentinel = Sentinel([('10.5.5.194', 26379),
                     ('10.5.5.155', 26379),
                     ('10.5.5.128', 26379), ], socket_timeout=0.5)

master = sentinel.master_for('mymaster', socket_timeout=0.5, password='root123', db=0)

name = sys.argv[2]

slave = sentinel.slave_for('mymaster', socket_timeout=0.5, password='root123', db=0)

# 判断是否所传参数对应的value值是否为空或者1，如果是设置为0
if slave.get(name) is None or slave.get(name) == "0":
    master.set(name, "1")
    f_do = sys.argv[1] + '.do'
    f_dat = sys.argv[1] + '.dat'
    f = open(f_dat,'w')
    f.write('0'+'\n')
    f.write('success'+'\n')
    f.write('set '+name+'为1 \n')
    f.close()
    f = open(f_do,'w')
    f.write('')
    f.close()