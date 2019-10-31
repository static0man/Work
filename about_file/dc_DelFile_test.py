#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------
# 脚本名称    : dc_DelFile.py
# 更新时间    : 2019/10/28 11:33
# 作者        : Huang Wei Feng
# 脚本描述    : 将某个目录及子目录下的某个文件名的文件删除，支持文件名为统配符
# 参数        : （1）文件名，可以多个（2）目录，可以多个（3）目录选项，是否包括子目录(True/False)
# 注意事项    :  多个文件名或目录名用逗号隔开
# -------------------------------------------------------

import sys
import os

FileName = sys.argv[2]
FilePath = sys.argv[3]
IsSubDir = sys.argv[4]

def EnumPathFiles(FilePath, callback):
    if not os.path.isdir(FilePath):
        print('Error:"', FilePath, '" is not a directory or does not exist.')
        return
    list_dirs = os.walk(FilePath)

    for root, dirs, files in list_dirs:
        for d in dirs:
            EnumPathFiles(os.path.join(root, d), callback)
        for f in files:
            callback(root, f)

def callback1(path, filename):
    print(path+'\\'+filename)

if __name__ == '__main__':
    EnumPathFiles(r'D:\Projects\python', callback1)