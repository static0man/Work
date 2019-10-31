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
import glob

Name = sys.argv[2]
Path = sys.argv[3]
IsSubDir = sys.argv[4]

# Path = r"C:\Users\HUANGWF\Desktop\work\test"
# Name = "name.txt,a*.log,b*.py"
# IsSubDir = False

def MenuDirFile(FilePath, FileNames):
    # 获取当前目录的所有文件夹和文件
    for Files in os.listdir(FilePath):
        # 获取当前文件夹路径
        FileNowPath = os.path.join(FilePath, Files)
        # print FileNowPath
        # 判读删除操作是否包含子目录
        if IsSubDir:
            # 判断是否为文件夹
            if os.path.isdir(FileNowPath):
                # 递归查找删除
                MenuDirFile(FileNowPath, FileNames)
            else:
                # 查找删除
                DelFile(Files, FileNames, FilePath)
        else:
            # 查找删除
            DelFile(Files, FileNames, FilePath)

def DelFile(Files, FileNames, FilePath):
    # 查找删除
    for FileName in FileNames:
        # 根据通配符匹配对应的文件名，输出为列表
        TFileNames = glob.glob(os.path.join(FilePath, FileName))
        # 遍历TFileNames
        for TFileName in TFileNames:
            # 判断文件路径是否符合传入文件名路径
            if TFileName == os.path.join(FilePath, Files):
                os.remove(TFileName)

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