#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------
# 脚本名称    : test3.py
# 更新时间    : 2019/10/31 15:58
# 作者        : Huang Wei Feng
# 脚本描述    : 
# 参数        :
# 注意事项    :  
# -------------------------------------------------------
FilePath = r'C:\Users\HUANGWF\Desktop\work\about_file\test.properties'
import sys
import os
import re
pattern = re.compile(r'' + 'a=.*')
with open(FilePath, 'r') as r:
    for line in r.readlines():
        print line
        a = pattern.match(line)
        print a
        line = re.sub(r'a=.*', 'a=www.baidu.com', line)
        print line
        print '========================='