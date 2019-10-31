#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------
# 脚本名称    : dc_UpdateAndDelXML.py
# 更新时间    : 2019/10/29 16:16
# 作者        : Huang Wei Feng
# 脚本描述    : 更新xml文件的节点、属性的内容，支持多个节点、属性信息更新
# 参数        : （1）文件目录（2）文件名（3）要更新的xml节点或属性、及值, （4）要删除的xml节点或属性
# 注意事项    :  
# -------------------------------------------------------

import sys
import os
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET
# Name = sys.argv[2]
# Path = sys.argv[3]
# UpdateEles = sys.argv[4]  # 节点名，节点值，属性，属性值（不修改的值填原值,名字对应的值可以为空，添加属性同时改属性名和属性值即可）
# DelEles = sys.argv[5]  # 节点名，属性名（不修改的值不填但要加逗号）
# XMLPath = os.path.join(Path, Name)
# OutPutName = "output_json"
# IsErr = True
# XmlEle = "./card/cardname\n./card/riverversion\n./card/subvendorid[@name]"
XMLPath = r"C:\Users\HUANGWF\Desktop\work\about_file\vga.xml"
UpdateEles = "./card/clockgpuboostdefault[@name='2'],11,name,222222"
DelEles = "./car,./card/driverversion[@name='2']"

def UpdateXml(tree, root, ele_update_list):
    # 更新修改数据
    # 遍历符合条件的节点
    for UpdateEle in root.findall(ele_update_list[0]):
        # 修改属性
        UpdateEle.set(ele_update_list[2], ele_update_list[3])
        # 修改节点值
        UpdateEle.text = ele_update_list[1]
        # 写入文件
        tree.write(XMLPath)
        print "节点{}修改成功".format(UpdateEle.tag)

def DelNode(tree, root):
    # 删除数据
    # 获取传入的节点参数
    ele_del_list = DelEles.split(",")
    # 判读所传参数是否为空
    if ele_del_list[0] == '':
        pass
    else:
        # 切片方式获取所需删除节点和其父节点
        ele_child_name = ele_del_list[0].split("/")[-1]
        ele_parent_name = ele_del_list[0].split("/")[-2]
        # 遍历符合条件的父节点
        for Parent in root.findall(ele_parent_name):
            # 遍历符合条件的子节点
            for DelEle in Parent.findall(ele_child_name):
                # 删除
                Parent.remove(DelEle)
                tree.write(XMLPath)
                print "节点{}删除成功".format(DelEle.tag)

    # 删除元素属性
    if ele_del_list[1] == '':
        pass
    else:
        # 切片方式获取所需删除节点和其父节点
        ele_child_name = ele_del_list[1].split("/")[-1]
        ele_parent_name = ele_del_list[1].split("/")[-2]
        # 遍历符合条件的父节点
        for Parent in root.findall(ele_parent_name):
            # 遍历符合条件的子节点
            for DelEle in Parent.findall(ele_child_name):
                # 删除属性
                # if key in DelEle.attrib:
                #     del DelEle.attrib[key]
















                tree.write(XMLPath)

def ReadXml():
    try:
        # 讲xml解析成树结构
        tree = ET.parse(XMLPath)
        # 获取根节点
        root = tree.getroot()
    except Exception as e:
        print e
    # 获取传入的节点参数
    ele_update_list = UpdateEles.split(",")
    # 更新数据
    UpdateXml(tree, root, ele_update_list)
    # 删除数据
    DelNode(tree, root)

if __name__ == '__main__':
    ReadXml()