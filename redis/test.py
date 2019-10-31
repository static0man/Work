#!/usr/bin/python
#coding:utf-8
import os
# filePath = '/files_judge'
# list = os.listdir(filePath)
# print(list)
name = "name"
filePath = '/files_judge'
if  os.path.exists(filePath) is False:
    make_dir = os.mkdir(filePath)
    with open("{}/{}.txt".format(filePath, name), "w"):
        pass
else:
    with open("{}/{}.txt".format(filePath, name), "w"):
        pass
import random

name_list = []
for name in range(50):
    name_list.append(str(name))
print name_list

try:
    import psutil
except:
    import os
    print "正在安装psutil模块~~~"
    os.system("pip2 install psutil")

    import psutil

print psutil.cpu_times()
pid_list = psutil.pids()
with open("./pid.txt", "a") as a:
    for pid in pid_list:
        p = psutil.Process(pid)
        a.write("="*5+"进程"+str(pid)+"="*5 + "\n")
        a.write(p.name() + "\n")
        a.write(str(p.environ()) + "\n")
        a.write(p.status() + "\n")

