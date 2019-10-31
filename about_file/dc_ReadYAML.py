#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------
# 脚本名称    : dc_ReadYAML.py
# 更新时间    : 2019/10/31 17:24
# 作者        : Huang Wei Feng
# 脚本描述    : 读取yaml文件的属性值
# 参数        : （1）文件目录（2）文件名（3）属性名，可以多个，用换行分隔（4）输出变量名（5）文件编码格式
# 注意事项    :  
# -------------------------------------------------------

import sys
import os

# Path = sys.argv[1] # -->文件路径
# Name = sys.argv[2] # -->文件名字
# AttrNames = sys.argv[3] # -->属性名
# OutPutName = sys.argv[4] # -->输出变量名
# Code = sys.argv[5] # -->文件编码格式
# FilePath = os.path.join(Path, Name) # -->完整路径
Code = 'utf-8'
AttrNames = 'username\npassword'
FilePath = r'C:\Users\HUANGWF\Desktop\work\about_file\test.yaml'

with open(FilePath, 'r') as r:
    a = r.readlines()
for i in a:
    print i.strip()