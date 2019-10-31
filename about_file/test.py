#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------
# 脚本名称    : test.py
# 更新时间    : 2019/10/28 10:46
# 作者  : Huang Wei Feng
# 脚本描述    : 
# 注意事项: 
# -------------------------------------------------------
import sys
import os

# Name = sys.argv[2]
# Path = sys.argv[3]
# IsSubDir = sys.argv[4]
Name = "name.txt"
Path = r"C:\Users\HUANGWF\Desktop\work\test"
IsSubDir = False
i = 0
def EnumPathFiles(FilePath,FileNames):
    # 获取目录的当前路径，子文件夹列表，文件列表
    for Root, Dirs, Files in os.walk(FilePath):
        # 删除文件时是否包含子目录
        if IsSubDir is True:
            for FileName in FileNames:
                if FileName in Files:
                    pass
                    #os.remove(os.path.join(Root, FileName))
            for Dir in Dirs:
                # 递归
                pass
                # EnumPathFiles(os.path.join(Root, Dir), FileNames)
        else:
            # 删除文件
            for FileName in FileNames:
                if FileName in Files:
                    print(FilePath)
                    os.remove(os.path.join(FilePath, FileName))

def main():
    # 获取传入的文件名和目录名的列表
    FileNames = Name.split(",")
    FilePaths = Path.split(",")
    # 遍历列表获取目录
    for FilePath in FilePaths:
        # 路径是否存在
        if not os.path.isdir(FilePath):
            print('Error:"', FilePath, '" is not a directory or does not exist.')
            return
        EnumPathFiles(FilePath, FileNames)
    print("over!")
if __name__ == '__main__':
    main()
