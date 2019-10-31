#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------
# 脚本名称    : test2.py
# 更新时间    : 2019/10/28 16:43
# 作者        : Huang Wei Feng
# 脚本描述    : 
# 参数        :
# 注意事项    :  
# -------------------------------------------------------

import sys
import os
import xml.etree.ElementTree as ET

XmlEle = "./card/cardname\n./card/driverversion\n./card/subvendorid[@name]"
XMLPath = r"C:\Users\HUANGWF\Desktop\work\about_file\vga.xml"
tree = ET.parse(XMLPath)
root = tree.getroot()
xpath_ele_list = XmlEle.split("\n")
for xpath_ele in xpath_ele_list:
    # 按xpath查找到符合的节点列表
    element_list = root.findall(xpath_ele)
    for a in element_list:
        root.remove(a)

