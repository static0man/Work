#!/usr/bin/python
# -*- coding:utf-8 -*-


#!/usr/bin/python
import redis
from redis.sentinel import Sentinel

# 连接哨兵服务器(主机名也可以用域名)
# sentinel = Sentinel([('10.5.5.194', 26379),
#                      ('10.5.5.155', 26379),
#                      ('10.5.5.128', 26379), ], socket_timeout=0.5)

#from redis import WatchError
MYSETINEL = None
MASTER = None
SLAVE = None

# 1.redis 哨兵模式集群最少需要一主三从, 三哨兵
# 2.redis 哨兵集群所有主从节点都完整的保存了一份数据
SENTINEADDRESS = [('10.5.5.194', 26379), ('10.5.5.155', 26379), ('10.5.5.128', 26379)]

def get_redis_conn():
    global MYSETINEL
    global MASTER
    global SLAVE
    # 如果哨兵连接实例已存在, 不重复连接, 当连接失效时, 重新连接
    if not MYSETINEL:# 连接哨兵
        MYSETINEL = Sentinel(SENTINEADDRESS, socket_timeout=2000)  # 尝试连接最长时间单位毫秒, 1000毫秒为1秒
        # 通过哨兵获取主数据库连接实例      参数1: 主数据库的名字(集群部署时在配置文件里指明)
        MASTER = MYSETINEL.master_for('mymaster', socket_timeout=2000)
        # 通过哨兵获取从数据库连接实例    参数1: 从数据的名字(集群部署时在配置文件里指明)
        SLAVE = MYSETINEL.slave_for('mymaster', socket_timeout=2000)
# 每次都先尝试生成连接实例
get_redis_conn()

# 往 主数据库 写入数据
def setcache(key, value):
    global MASTER
    if MASTER:
        return MASTER.set(key, value)
    else:
        return False

# 从 从数据库 读取数据
def getcache(key):
    global SLAVE
    if SLAVE:
        return SLAVE.get(key)
    else:
        return False