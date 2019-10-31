#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------
# 脚本名称    : dc_ReadProperties.py
# 更新时间    : 2019/10/31 11:56
# 作者        : Huang Wei Feng
# 脚本描述    : 读取properties文件的属性值
# 参数        : （1）文件目录（2）文件名（3）属性名，可以多个，用换行分隔（4）输出变量名（5）文件编码格式
# 注意事项    :  
# -------------------------------------------------------
import re
import os
import tempfile
import json

# Path = sys.argv[1] # -->文件路径
# Name = sys.argv[2] # -->文件名字
# AttrNames = sys.argv[3] # -->属性名
# OutPutName = sys.argv[4] # -->输出变量名
# Code = sys.argv[5] # -->文件编码格式
# FilePath = os.path.join(Path, Name) # -->完整路径
Code = 'utf-8'
AttrNames = 'username\npassword'
FilePath = r'C:\Users\HUANGWF\Desktop\work\about_file\test.properties'

class Properties:

    def __init__(self, file_name):
        '''
        初始化
        file_name：文件名称
        '''
        self.file_name = file_name
        # 初始化一个空字典
        self.properties = {}
        try:
            # 读文件
            fopen = open(self.file_name, 'r')
            # 遍历内容行
            for line in fopen:
                # 去空格
                line = line.strip()
                # 剔除注释行
                if line.find('=') > 0 and not line.startswith('#'):
                    # 分割key和value
                    strs = line.split('=')
                    # 写入字典
                    self.properties[strs[0].strip()] = strs[1].strip()
        except Exception, e:
            raise e
        else:
            fopen.close()

    def Has_Key_func(self, key):
        '''是否存在key，返回boll值'''
        return key in self.properties

    def Get_func(self, key, default_value=''):
        '''
        获取对应key的value值
        key：键名
        default_value：默认值
        '''
        # 判断key是否存在
        if key in self.properties:
            # 返回对应键的value值
            return self.properties[key]
        # 不存在则返回默认值
        return default_value

    def Put_func(self, key, value):
        '''
        更新修改文件
        :param key: 指定键
        :param value: 指定键对应的value值
        '''
        self.properties[key] = value
        Replace_Property(self.file_name, key + '=.*', key + '=' + value, True)


def Parse(file_name):
    '''获取文件内容'''
    return Properties(file_name)


def Replace_Property(file_name, from_regex, to_str, append_on_not_exists=True):
    '''
    数据处理
    :param file_name: 文件完整路径
    :param from_regex: 正则表达式
    :param to_str: 键值对字符串
    :param append_on_not_exists: 是否新添加标记符
    '''
    # 获取tempfile实例对象
    tmpfile = tempfile.TemporaryFile()
    # 判断文件是否存在
    if os.path.exists(file_name):
        # 读文件
        r_open = open(file_name, 'r')
        # 正则表达式（以字符串书写的）转换为模式对象，可以实现更加有效的匹配
        # 返回满足正则的pattern对象
        pattern = re.compile(r'' + from_regex)
        found = None
        # 遍历行
        for line in r_open:
            # 匹配每行，返回符合正则条件的第一个，不成功返回None；剔除注释行
            # 注意，如果用pattern.seach()可能会对单字符属性匹配错误
            if pattern.match(line) and not line.strip().startswith('#'):
                found = True
                # 用指定键值对替换该行
                line = re.sub(from_regex, to_str, line)
            # 向临时文件中写入替换后的行内容
            tmpfile.write(line)
        # 如果没有匹配到和新添加标记符为true，则往临时文件里添加一行新数据
        if not found and append_on_not_exists:
            tmpfile.write('\n' + to_str)
        r_open.close()
        # 从头读取，和一般文件对象不同，seek方法的执行不能少
        tmpfile.seek(0)
        # 读取临时文件内容
        content = tmpfile.read()
        # 判断文件是否存在
        if os.path.exists(file_name):
            # 存在则删除文件
            os.remove(file_name)
        # 新建原指定文件名的文件，并写入临时文件读取的数据
        w_open = open(file_name, 'w')
        w_open.write(content)
        w_open.close()
        # 关闭临时文件同时删除该文件
        tmpfile.close()
    else:
        print "file %s not found" % file_name


if __name__ == '__main__':
    # 读取文件
    props = Parse(FilePath)
    # 定义一个空字典
    Dict = {}
    # 切割传入指定键名字符串
    for Key in AttrNames.split("\n"):
        # 根据key读取value
        Value = props.Get_func(Key)
        # 存入字典中
        Dict[Key] = Value
    # 把字典转换为json格式
    OutPutName = json.dumps(Dict)
    print OutPutName