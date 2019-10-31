#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------
# 脚本名称    : dc_ReadINI.py
# 更新时间    : 2019/10/30 17:42
# 作者        : Huang Wei Feng
# 脚本描述    : 读取ini文件中指定段的键值
# 参数        : （1）文件目录（2）文件名(3)指定段（4）属性键（5）输出变量名（6）文件编码
# 注意事项    :  
# -------------------------------------------------------

import sys
import os
import ConfigParser

def main():
    # Path = sys.argv[1] # -->文件路径
    # Name = sys.argv[2] # -->文件名字
    # Sections = sys.argv[3] # -->指定段
    # Key = sys.argv[4] # -->指定键
    # OutPutName = sys.argv[5] # -->输出名
    # Code = sys.argv[6]
    # FilePath = os.path.join(Path, Name) # -->完整路径
    Code = 'utf-8'
    Key = 'Name'
    Sections = 'ZIP'
    FilePath = r'C:\Users\HUANGWF\Desktop\work\about_file\test.ini'
    conf = ConfigParser.ConfigParser()
    conf.read(FilePath)
    # 获取文件所有sections
    sections = conf.sections()
    print "sections: {}".format(sections)
    if conf.has_section(Sections):
        # 获取指定段的所有键值对列表
        KeyValues = conf.items(Sections)
        print "key,value outside of ZIP: {}".format(KeyValues)
        # 获取指定段的指定键的值
        Value = conf.get(Sections, Key)
        print Value
        print "{} value is: {}".format(Key, Value)
        # 把键值保存到一个字典中
        OutPutName = {Key: Value}
        print OutPutName
    else:
        print "sections {} is notfind!".format(Sections)

if __name__ == '__main__':
    main()
