#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET
XMLPath = r"C:\Users\HUANGWF\Desktop\work\about_file\vga.xml"

# 讲xml解析成树结构
tree = ET.parse(XMLPath)
# 获取根节点
root = tree.getroot()
s = './car/clockgpu/adaf/dafdsf/afdf'
l = s.split("/")

a = root.findall("/".join(l[:-1]))

if a==[]:
    element = Element(l[1])
    for i in range(1, len(l)):
        if root.findall("/".join(l[:i])) == [] and i <len(l)-1:
            one = Element(l[i])
            tow = Element(l[i+1])
            print "/".join(l[:i])
            print '节点{}不存在,需创建！'.format("/".join(l[:i]))
            one.append(tow)
    root.append(element)
    tree.write(XMLPath)

#一级
# element = Element(l[1],)
# #二级
#     one = Element(l[2],)
#         tow = Element(l[3],)
#         tow.text = "222222"
#     element.append(one)
# one.append(tow)
# root.append(element)
# tree.write(XMLPath)





