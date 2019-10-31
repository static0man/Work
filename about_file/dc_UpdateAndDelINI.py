#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------
# 脚本名称    : dc_UpdateAndDelINI.py
# 更新时间    : 2019/10/31 10:09
# 作者        : Huang Wei Feng
# 脚本描述    : 修改ini文件中指定段的键值、增加新的键值、删除键值
# 参数        : （1）文件目录（2）文件名（3）指定段，文件中没有就增加该段（4）要更新或者新增的属性键值,可以多个用英文逗号隔开
#               （5）要删除的属性键,可以多个用英文逗号隔开,不删除则传0（6）文件编码
# 注意事项    :  
# -------------------------------------------------------

import sys
import os
import ConfigParser

# Path = sys.argv[1] # -->文件路径
# Name = sys.argv[2] # -->文件名字
# Sections = sys.argv[3] # -->指定段
# KeyValues = sys.argv[4] # -->指定键值
# DelKeys = sys.argv[5] # -->指定删除的键
# Code = sys.argv[6]
# FilePath = os.path.join(Path, Name) # -->完整路径
Code = 'utf-8'
KeyValues = "Name1:小黄,Name:小黄"
DelKeys = 'Name,text,Name1'
Sections = 'ZIP'
FilePath = r'C:\Users\HUANGWF\Desktop\work\about_file\test.ini'

def Key_Update_func(conf):
    '''更新和新添
    conf：ConfigParser实例对象'''
    if conf.has_section(Sections):
        # 获取指定段的所有键值对列表
        Items = conf.items(Sections)
        print "key,value outside of ZIP: {}\n".format(Items)
        # 把传入的键值字符串切割为key和value
        for KeyValue in KeyValues.split(","):
            Key = KeyValue.split(":")[0]
            Value = KeyValue.split(":")[1]
            # 设置指定段的指定键的值
            conf.set(Sections, Key, Value)
            conf.write(open(FilePath, 'w'))
            print "Update {} success!\n".format(Key)
    else:
        conf.add_section(Sections)
        # 获取指定段的所有键值对列表
        Items = conf.items(Sections)
        print "key,value outside of ZIP: {}\n".format(Items)
        print "Add sections {} Sucess!\n".format(Sections)
        # 把传入的键值字符串切割为key和value
        for KeyValue in KeyValues.split(","):
            Key = KeyValue.split(":")[0]
            Value = KeyValue.split(":")[1]
            # 设置指定段的指定键的值
            conf.set(Sections, Key, Value)
            conf.write(open(FilePath, 'w'))
            print "Update {} success!\n".format(Key)

def Key_Del_func(conf):
    '''删除指定键
    conf：ConfigParser实例对象'''
    # 遍历所传入的需要删除的键
    for DelKey in DelKeys.split(","):
        # 判断是否为0，true为不删除
        if DelKey == "0":
            pass
        else:
            # 判断对应段是否存在该键
            if conf.has_option(Sections, DelKey):
                # 删除键
                conf.remove_option(Sections, DelKey)
                # 保存
                conf.write(open(FilePath, 'w'))
                print "Delete {}'s {} Success!\n".format(Sections, DelKey)
            else:
                print "{}'s {} Not Find!\n".format(Sections, DelKey)

def main():
    conf = ConfigParser.ConfigParser()
    conf.read(FilePath)
    # 获取文件所有sections
    sections = conf.sections()
    print "The iniFile has sections: {}\n".format(sections)
    # 更新或添加
    Key_Update_func(conf)
    # 删除
    Key_Del_func(conf)

if __name__ == '__main__':
    main()
