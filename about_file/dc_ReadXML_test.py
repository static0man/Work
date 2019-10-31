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

from lxml import etree
def parsexml():
     tree=etree.parse(r"C:\Users\HUANGWF\Desktop\work\about_file\vga.xml")
     a = tree.xpath('card/cardname')
     for box in a:
         print(box.text)
def main():
      parsexml()
if __name__ == '__main__':
        main()