#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------
# 脚本名称    : dc_JudgeFile.py
# 更新时间    : 2019/10/28 11:15
# 作者        : Huang Wei Feng
# 脚本描述    : 判断指定文件名的文件是否存在，支持一定格式的动态文件名（如日期格式）
# 参数        : （1）文件名（2）目录
# 注意事项    :  
# -------------------------------------------------------

import sys
import os

def main():
    FileName = sys.argv[2]
    FilePath = sys.argv[3]
    if os.path.exists(os.path.join(FilePath, FileName)):
        print("文件存在")
    else:
        print("文件不存在")

if __name__ == '__main__':
    main()