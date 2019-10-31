#!/usr/bin/python
# coding=utf-8
from multiprocessing import Pool
from redis.sentinel import Sentinel

# 连接哨兵服务器(主机名也可以用域名)
sentinel = Sentinel([('10.5.5.194', 26379),
                     ('10.5.5.155', 26379),
                     ('10.5.5.128', 26379), ], socket_timeout=0.5)
# # 获取主服务器地址
# master = sentinel.discover_master('mymaster')
# print(master)
# # 输出：('172.31.0.2', 5001)
# # 获取从服务器地址
# slave = sentinel.discover_slaves('mymaster')
# print(slave)
# # 输出：[('172.31.3', 5001), ('172.31.0.4', 5001), ('172.31.0.5', 5001)]
# # 获取主服务器进行写入
master = sentinel.master_for('mymaster', socket_timeout=0.5, password='root123', db=0)
# # 输出：True
# 初始化
def init_data():
    master = sentinel.master_for('mymaster', socket_timeout=0.5, password='root123', db=0)
    for x in range(5):
        for y in range(1000):
            for i in range(1, 11):
                name = "app" + str(x) + "_wf" + str(y).zfill(5) + "_value" + str(i*10-1).zfill(3)
                value = "0"
                master.set(name, value)

if __name__ == "__main__":
    po = Pool(10)
    po.apply_async(init_data, )
    po.close()
    po.join()