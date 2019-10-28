#!/usr/bin/python
# coding=utf-8
# ----------------------
# @Time    : 2019/10/28 19:55
# @Author  : hwf
# @File    : dc_DelFiles1.py
# ----------------------

import sys
import os

Path = r"C:\Users\hwf\Desktop\work_test\file_test"
Name = "name.txt"
IsSubDir = False


def endWith(*endstring):
    # 通配符方式查找文件
    ends = endstring
    def run(s):
        f = map(s.endswith, ends)
        if True in f: return s
    return run


# if __name__ == '__main__':
#     import os
#
#     list_file = os.listdir('/root')
#     a = endWith('.txt', '.py')
#     f_file = filter(a, list_file)
#     for i in f_file: print i

def MenuDirFile(FilePath, FileNames):
    # 获取当前目录的所有文件夹和文件
    for Files in os.listdir(FilePath):
        # 获取当前文件夹路径
        FileNowPath = os.path.join(FilePath, Files)
        print FileNowPath
        # 判读删除操作是否包含子目录
        if IsSubDir:
            # 判断是否为文件夹
            if os.path.isdir(FileNowPath):
                # 递归查找删除
                MenuDirFile(FileNowPath, FileNames)
            else:
                # 查找删除
                DelFile(Files, FileNames, FileNowPath)
        else:
            # 查找删除
            DelFile(Files, FileNames, FileNowPath)

def DelFile(Files, FileNames, FileNowPath):
    # 查找删除
    for FileName in FileNames:
        if FileName == Files:
            os.remove(FileNowPath)

def main():
    FilePaths = Path.split(",")
    FileNames = Name.split(",")
    for FilePath in FilePaths:
        # 判断文件路径是否存在
        if not os.path.exists(FilePath):
            print "{} directory does not exist".format(FilePath)
            return
        MenuDirFile(FilePath, FileNames)

if __name__ == "__main__":
    main()