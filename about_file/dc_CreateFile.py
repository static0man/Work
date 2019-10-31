#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------
# 脚本名称    : dc_CreateFile.py
# 更新时间    : 2019/10/28 10:46
# 作者        : Huang Wei Feng
# 脚本描述    : 在指定目录下创建一个文件，并写入初始数据
# 参数        :（1）文件名（2）目录（3）内容
# 注意事项    :
# -------------------------------------------------------

import sys
import os

def main():
    FileName = sys.argv[2]
    FilePath = sys.argv[3]
    FileContent = sys.argv[4]
    # 目标目录是否存在
    if os.path.exists(FilePath):
        with open(os.path.join(FilePath, FileName), 'w') as a:
            a.write(FileContent)
    else:
        print("目录不存在")

if __name__ == "__main__":
    main()
