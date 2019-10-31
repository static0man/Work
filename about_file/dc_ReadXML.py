#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------
# 脚本名称    : dc_ReadXML.py
# 更新时间    : 2019/10/29 10:36
# 作者        : Huang Wei Feng
# 脚本描述    : 读取xml文件的节点、属性的内容，支持多个节点、属性信息读取
# 输入        : （1）文件名（2）文件目录（3）要读取的xml节点或属性，采用xpath格式，可以多个，多个用换行符分隔”（4）输出变量名（5）未找到时是否表示操作失败
# 输出        : （1）成功或失败（2）节点和属性的值，JSON格式，带上节点和属性名
# 注意事项    :  
# -------------------------------------------------------

import sys
import os
import xml.etree.ElementTree as ET
import json
Name = sys.argv[2]
Path = sys.argv[3]
XmlEle = sys.argv[4]
OutPutName = sys.argv[5]
IsErr = sys.argv[6]
XMLPath = os.path.join(Path, Name)
# OutPutName = "output_json"
# IsErr = True
# XmlEle = "./card/cardname\n./card/riverversion\n./card/subvendorid[@name]"
# XMLPath = r"C:\Users\HUANGWF\Desktop\work\about_file\vga.xml"

def ReadXml():
    try:
        # 讲xml解析成树结构
        root = ET.parse(XMLPath)
    except Exception as e:
        print e

    # 对传入的xpath进行分割
    xpath_ele_list = XmlEle.split("\n")
    for xpath_ele in xpath_ele_list:
        # 按xpath查找到符合的节点列表
        element_list = root.findall(xpath_ele)
        # 判断节点是否存在
        if element_list == [] and IsErr:
            print "Xpath: {} is notfind!".format(xpath_ele)
        # 遍历列表
        for element in element_list:
            # 获取节点数据或属性
            ele_name = element.tag  # -->str
            ele_val = element.text  # -->str
            attr = element.attrib  # -->dict
            # 把获取的数据以字典方式存储
            ele_dict = dict({ele_name: ele_val}, **attr)  # 合并两字典
            # 把字典转换成json数据输出
            OutPutName = json.dumps(ele_dict)
            print OutPutName

if __name__ == '__main__':
    ReadXml()