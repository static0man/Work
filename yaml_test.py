#!/usr/bin/python
# coding=utf-8
# ----------------------
# @Time    : 2019/11/3 18:17
# @Author  : hwf
# @File    : yaml_test.py
# ----------------------

import yaml
name = 'a1/children/[1]/a2/children1/[1]/name1'
path = r"C:\Users\hwf\Desktop\work_test\yaml.yaml"

class YamlObj():
    def __init__(self, key):
        self.key = key

    def creat_list(self):
        yaml_obj = []


yaml_obj = yaml.load(open(path, 'r'), Loader=yaml.FullLoader)

keys = name.split('/')
a = yaml_obj[keys[0]]
print a
global b
b = yaml_obj[keys[0]]
print b
print type(b)

for key in keys[1:]:
    if key.startswith("["):
        key = int(key[1:-1])
        b = b[key]
        print("{}： {}".format(key, b))
    else:
        b = b[key]
        print("{}： {}".format(key, b))
print b