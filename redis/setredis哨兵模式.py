#!/usr/bin/env python
# -*- coding:utf-8 -*-


#!/usr/bin/env python
import redis
from redis.sentinel import Sentinel

# 连接哨兵服务器(主机名也可以用域名)
sentinel = Sentinel([('10.5.5.194', 26379),
                     ('10.5.5.155', 26379),
                     ('10.5.5.128', 26379), ], socket_timeout=0.5)
# 获取主服务器地址
master = sentinel.discover_master('mymaster')
print(master)
# 输出：('172.31.0.2', 5001)

# 获取从服务器地址
slave = sentinel.discover_slaves('mymaster')
print(slave)
# 输出：[('172.31.3', 5001), ('172.31.0.4', 5001), ('172.31.0.5', 5001)]

# 获取主服务器进行写入
master = sentinel.master_for('mymaster', socket_timeout=0.5, password='root123', db=0)
w_ret = master.set('name', 'myredis is redis')
# 输出：True

# # 获取从服务器进行读取
slave = sentinel.slave_for('mymaster', socket_timeout=0.5, password='root123', db=0)
r_ret = slave.get('name')
print(r_ret)
