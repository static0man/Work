#!/usr/bin/python
# coding=utf-8

# 导入第三方模块
try:
    from xlutils.copy import copy
    import xlrd
    import xlwt
except :
    print("正在安装模块！")
    import os
    os.system('pip install xlrd ; pip install xlwt ; pip install xlutils')
    from xlutils.copy import copy
    import xlrd
    import xlwt

from multiprocessing import Pool
import sys


# 参考文件路径
# parent_file_path = sys.argv[1]

parent_file_path = './app4_wf00000TEM.xls'
# 先打开已存在的表,保持原有格式
oldWorkbook = xlrd.open_workbook(parent_file_path, formatting_info=True)
# 复制xls文件
def copy_xls(xls_name):
    # 复制
    newWorkbook = copy(oldWorkbook)

    # 取第一个sheet表，修改表（0~6）

    for sheet in oldWorkbook.sheets():
        # 修改
        sheet_num = oldWorkbook.sheets().index(sheet)
        # print("==============" + str(sheet_num) + "========")
        modify_file_content(sheet_num, xls_name, newWorkbook)
        # print("save over")
    # 保存
    newWorkbook.save(r'./excel/' + xls_name + '.xls')

# 表一，表二
def sheet1(sheet_num, xls_name, newworkbook):
    newworksheet = newworkbook.get_sheet(sheet_num)
    # 修改第3行第一列
    newworksheet.write(2, 0, xls_name)

# 表三
def sheet3(sheet_num, xls_name, newworkbook):
    newworksheet = newworkbook.get_sheet(sheet_num)
    # 获取表的有效行数
    nrows = oldWorkbook.sheets()[sheet_num].nrows
    str_list = xls_name.split("_")
    for nrow in range(3, nrows):
        # 写入
        # app1
        if str_list[0] == "app1":
            if nrow <= 102:
                newworksheet.write(nrow, 0, xls_name + '_job' + str(nrow - 3).zfill(3), cell_style())
            elif 103 <= nrow <= 112:
                # str_list = xls_name.split("_")
                # xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(
                #     (nrow - 100) * 10 - 21).zfill(3)
                newworksheet.write(nrow, 0, xls_name + "_value" + str((nrow - 100) * 10 - 21).zfill(3), cell_style())
            else:
                # newworksheet.write(nrow, 0, xls_name + "_value" + str((nrow - 110) * 10 - 21).zfill(3), cell_style())
                del_nrow(sheet_num, newworksheet, nrow)

            newworksheet.write(nrow, 1, xls_name, cell_style())
            newworksheet.write(nrow, 2, xls_name.split('_')[0], cell_style())

            if 103 <= nrow <= 112:
                # str_list = xls_name.split("_")
                # xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(
                #     (nrow - 100) * 10 - 21).zfill(3)
                newworksheet.write(nrow, 9, "卡中心/事件依赖", cell_style())
                newworksheet.write(nrow, 10, xls_name + "_value" + str((nrow - 100) * 10 - 21).zfill(3), cell_style())
                # newworksheet.write(nrow, 10, "", cell_style())
            elif 113 <= nrow <= 122:
                for i in range(15):
                    newworksheet.write(nrow, i, "", cell_style())
                # newworksheet.write(nrow, 10, xls_name + "_value" + str((nrow - 110) * 10 - 21).zfill(3), cell_style())

        # app5
        elif str_list[0] == "app5":
            if nrow <= 102:
                newworksheet.write(nrow, 0, xls_name + '_job' + str(nrow - 3).zfill(3), cell_style())
            elif 103 <= nrow <= 112:
                # str_list = xls_name.split("_")
                xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(
                    (nrow - 100) * 10 - 21).zfill(3)
                newworksheet.write(nrow, 0, xls_name1, cell_style())
            else:
                # newworksheet.write(nrow, 0, xls_name + "_value" + str((nrow - 110) * 10 - 21).zfill(3), cell_style())
                newworksheet.write(nrow, 0, "", cell_style())

            newworksheet.write(nrow, 1, xls_name, cell_style())
            newworksheet.write(nrow, 2, xls_name.split('_')[0], cell_style())

            if 103 <= nrow <= 112:
                # str_list = xls_name.split("_")
                xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(
                    (nrow - 100) * 10 - 21).zfill(3)
                newworksheet.write(nrow, 10, xls_name1, cell_style())
            elif 113 <= nrow <= 122:
                # newworksheet.write(nrow, 10, xls_name + "_value" + str((nrow - 110) * 10 - 21).zfill(3), cell_style())
                for i in range(15):
                    newworksheet.write(nrow, i, "", cell_style())

        # app2~app4
        else:
            if nrow <= 102:
                newworksheet.write(nrow, 0, xls_name + '_job' + str(nrow - 3).zfill(3), cell_style())
            elif 103 <= nrow <= 112:
                # str_list = xls_name.split("_")
                xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str((nrow - 100) * 10 - 21).zfill(3)
                newworksheet.write(nrow, 0, xls_name1, cell_style())
            else:
                newworksheet.write(nrow, 0, xls_name+"_value" + str((nrow - 110) * 10 - 21).zfill(3), cell_style())

            newworksheet.write(nrow, 1, xls_name, cell_style())
            newworksheet.write(nrow, 2, xls_name.split('_')[0], cell_style())

            if 103 <= nrow <= 112:
                # str_list = xls_name.split("_")
                xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str((nrow - 100) * 10 - 21).zfill(3)
                newworksheet.write(nrow, 10, xls_name1, cell_style())
            elif 113 <= nrow <= 122:
                newworksheet.write(nrow, 10, xls_name + "_value" + str((nrow - 110) * 10 - 21).zfill(3), cell_style())

# 表四
def sheet4(sheet_num, xls_name, newworkbook):
    newworksheet = newworkbook.get_sheet(sheet_num)
    # 获取表的有效行数
    nrows = oldWorkbook.sheets()[sheet_num].nrows
    str_list = xls_name.split("_")
    for nrow in range(2, nrows):
        # 写入
        # app1
        if str_list[0] == "app1":
            # 第一列
            newworksheet.write(nrow, 0, xls_name, cell_style())
            # 第二列
            # str_list = xls_name.split("_")
            if nrow <= 101:
                newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 2).zfill(3), cell_style())

            elif 102 <= nrow <= 111:
                newworksheet.write(nrow, 1, xls_name + "_value" + str((nrow - 100) * 10 - 11).zfill(3), cell_style())
            elif 112 <= nrow <= 121:
                newworksheet.write(nrow, 1, '开始', cell_style())
            else:
                del_nrow(sheet_num, newworksheet, nrow)

            # 第三列
            if nrow <= 101:
                if 2 <= nrow <= 10:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 1).zfill(3), cell_style())
                elif nrow == 11:
                    xls_name1 = xls_name + "_value" + str(9).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 12 <= nrow <= 20:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 1).zfill(3), cell_style())
                elif nrow == 21:
                    xls_name1 = xls_name + "_value" + str(19).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 22 <= nrow <= 30:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 1).zfill(3), cell_style())
                elif nrow == 31:
                    xls_name1 = xls_name + "_value" + str(29).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 32 <= nrow <= 40:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 1).zfill(3), cell_style())
                elif nrow == 41:
                    xls_name1 = xls_name + "_value" + str(39).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 42 <= nrow <= 50:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 1).zfill(3), cell_style())
                elif nrow == 51:
                    xls_name1 = xls_name + "_value" + str(49).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 52 <= nrow <= 60:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 1).zfill(3), cell_style())
                elif nrow == 61:
                    xls_name1 = xls_name + "_value" + str(59).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 62 <= nrow <= 70:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 1).zfill(3), cell_style())
                elif nrow == 71:
                    xls_name1 = xls_name + "_value" + str(69).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 72 <= nrow <= 80:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 1).zfill(3), cell_style())
                elif nrow == 81:
                    xls_name1 = xls_name + "_value" + str(79).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 82 <= nrow <= 90:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 1).zfill(3), cell_style())
                elif nrow == 91:
                    xls_name1 = xls_name + "_value" + str(89).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 92 <= nrow <= 100:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 1).zfill(3), cell_style())
                else:
                    xls_name1 = xls_name + "_value" + str(99).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())

            elif 102 <= nrow <= 111:
                newworksheet.write(nrow, 2, '结束', cell_style())
            elif 112 <= nrow <= 121:
                # xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(
                #     (nrow - 120) * 10 - 11).zfill(3)
                newworksheet.write(nrow, 2, xls_name + '_job' + str((nrow - 110) * 10 - 20).zfill(3), cell_style())
            else:
                for i in range(10):
                    newworksheet.write(nrow, i, '', cell_style())


        # app5
        elif str_list[0] == "app5":
            # 第一列
            newworksheet.write(nrow, 0, xls_name, cell_style())
            # 第二列
            # str_list = xls_name.split("_")
            if nrow <= 111:
                if nrow == 2:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(9).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 3 <= nrow <= 12:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 3).zfill(3), cell_style())
                elif nrow == 13:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(19).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 14 <= nrow <= 23:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 4).zfill(3), cell_style())
                elif nrow == 24:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(29).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 25 <= nrow <= 34:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 5).zfill(3), cell_style())
                elif nrow == 35:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(39).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 36 <= nrow <= 45:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 6).zfill(3), cell_style())
                elif nrow == 46:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(49).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 47 <= nrow <= 56:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 7).zfill(3), cell_style())
                elif nrow == 57:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(59).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 58 <= nrow <= 67:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 8).zfill(3), cell_style())
                elif nrow == 68:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(69).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 69 <= nrow <= 78:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 9).zfill(3), cell_style())
                elif nrow == 79:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(79).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 80 <= nrow <= 89:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 10).zfill(3), cell_style())
                elif nrow == 90:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(89).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 91 <= nrow <= 100:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 11).zfill(3), cell_style())
                elif nrow == 101:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(99).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                else:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 12).zfill(3), cell_style())

            elif 112 <= nrow <= 121:
                newworksheet.write(nrow, 1, '开始', cell_style())
            else:
                for i in range(10):
                    newworksheet.write(nrow, i, "", cell_style())

            # 第三列
            if nrow <= 111:
                if 2 <= nrow <= 11:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 2).zfill(3), cell_style())
                elif nrow == 12:
                    # xls_name1 = xls_name + "_value" + str(9).zfill(3)
                    newworksheet.write(nrow, 2, "结束", cell_style())
                elif 13 <= nrow <= 22:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 3).zfill(3), cell_style())
                elif nrow == 23:
                    # xls_name1 = xls_name + "_value" + str(19).zfill(3)
                    newworksheet.write(nrow, 2, "结束", cell_style())
                elif 24 <= nrow <= 33:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 4).zfill(3), cell_style())
                elif nrow == 34:
                    # xls_name1 = xls_name + "_value" + str(29).zfill(3)
                    newworksheet.write(nrow, 2, "结束", cell_style())
                elif 35 <= nrow <= 44:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 5).zfill(3), cell_style())
                elif nrow == 45:
                    # xls_name1 = xls_name + "_value" + str(39).zfill(3)
                    newworksheet.write(nrow, 2, "结束", cell_style())
                elif 46 <= nrow <= 55:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 6).zfill(3), cell_style())
                elif nrow == 56:
                    # xls_name1 = xls_name + "_value" + str(49).zfill(3)
                    newworksheet.write(nrow, 2, "结束", cell_style())
                elif 57 <= nrow <= 66:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 7).zfill(3), cell_style())
                elif nrow == 67:
                    # xls_name1 = xls_name + "_value" + str(59).zfill(3)
                    newworksheet.write(nrow, 2, "结束", cell_style())
                elif 68 <= nrow <= 77:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 8).zfill(3), cell_style())
                elif nrow == 78:
                    # xls_name1 = xls_name + "_value" + str(69).zfill(3)
                    newworksheet.write(nrow, 2, "结束", cell_style())
                elif 79 <= nrow <= 88:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 9).zfill(3), cell_style())
                elif nrow == 89:
                    # xls_name1 = xls_name + "_value" + str(79).zfill(3)
                    newworksheet.write(nrow, 2, "结束", cell_style())
                elif 90 <= nrow <= 99:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 10).zfill(3), cell_style())
                elif nrow == 100:
                    # xls_name1 = xls_name + "_value" + str(89).zfill(3)
                    newworksheet.write(nrow, 2, "结束", cell_style())
                elif 101 <= nrow <= 110:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 11).zfill(3), cell_style())
                else:
                    # xls_name1 = xls_name + "_value" + str(99).zfill(3)
                    newworksheet.write(nrow, 2, "结束", cell_style())
            elif 112 <= nrow <= 121:
                xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str((nrow - 110) * 10 - 11).zfill(3)
                newworksheet.write(nrow, 2, xls_name1, cell_style())
            else:
                # newworksheet.write(nrow, 2, '', cell_style())
                pass

        # app2~app4
        else:
            # 第一列
            newworksheet.write(nrow, 0, xls_name, cell_style())
            # 第二列
            # str_list = xls_name.split("_")
            if nrow <= 111:
                if nrow == 2:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(9).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 3 <= nrow <= 12:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 3).zfill(3), cell_style())
                elif nrow == 13:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(19).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 14 <= nrow <= 23:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 4).zfill(3), cell_style())
                elif nrow == 24:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(29).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 25 <= nrow <= 34:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 5).zfill(3), cell_style())
                elif nrow == 35:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(39).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 36 <= nrow <= 45:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 6).zfill(3), cell_style())
                elif nrow == 46:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(49).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 47 <= nrow <= 56:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 7).zfill(3), cell_style())
                elif nrow == 57:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(59).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 58 <= nrow <= 67:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 8).zfill(3), cell_style())
                elif nrow == 68:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(69).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 69 <= nrow <= 78:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 9).zfill(3), cell_style())
                elif nrow == 79:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(79).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 80 <= nrow <= 89:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 10).zfill(3), cell_style())
                elif nrow == 90:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(89).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                elif 91 <= nrow <= 100:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 11).zfill(3), cell_style())
                elif nrow == 101:
                    xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(99).zfill(3)
                    newworksheet.write(nrow, 1, xls_name1, cell_style())
                else:
                    newworksheet.write(nrow, 1, xls_name + '_job' + str(nrow - 12).zfill(3), cell_style())

            elif 112 <= nrow <= 121:
                newworksheet.write(nrow, 1, xls_name + "_value" + str((nrow-110)*10-11).zfill(3), cell_style())
            else:
                newworksheet.write(nrow, 1, '开始', cell_style())

            # 第三列
            if nrow <= 111:
                if 2 <= nrow <= 11:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 2).zfill(3), cell_style())
                elif nrow == 12:
                    xls_name1 = xls_name + "_value" + str(9).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 13 <= nrow <= 22:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 3).zfill(3), cell_style())
                elif nrow == 23:
                    xls_name1 = xls_name + "_value" + str(19).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 24 <= nrow <= 33:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 4).zfill(3), cell_style())
                elif nrow == 34:
                    xls_name1 = xls_name + "_value" + str(29).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 35 <= nrow <= 44:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 5).zfill(3), cell_style())
                elif nrow == 45:
                    xls_name1 = xls_name  + "_value" + str(39).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 46 <= nrow <= 55:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 6).zfill(3), cell_style())
                elif nrow == 56:
                    xls_name1 = xls_name  + "_value" + str(49).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 57 <= nrow <= 66:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 7).zfill(3), cell_style())
                elif nrow == 67:
                    xls_name1 = xls_name  + "_value" + str(59).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 68 <= nrow <= 77:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 8).zfill(3), cell_style())
                elif nrow == 78:
                    xls_name1 = xls_name  + "_value" + str(69).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 79 <= nrow <= 88:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 9).zfill(3), cell_style())
                elif nrow == 89:
                    xls_name1 = xls_name  + "_value" + str(79).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 90 <= nrow <= 99:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 10).zfill(3), cell_style())
                elif nrow == 100:
                    xls_name1 = xls_name  + "_value" + str(89).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
                elif 101 <= nrow <= 110:
                    newworksheet.write(nrow, 2, xls_name + '_job' + str(nrow - 11).zfill(3), cell_style())
                else:
                    xls_name1 = xls_name  + "_value" + str(99).zfill(3)
                    newworksheet.write(nrow, 2, xls_name1, cell_style())
            elif 112 <= nrow <= 121:
                newworksheet.write(nrow, 2, '结束', cell_style())
            else:
                xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str((nrow-120)*10-11).zfill(3)
                newworksheet.write(nrow, 2, xls_name1, cell_style())

# 表五
def sheet5(sheet_num, xls_name, newworkbook):
    pass

# 表六
def sheet6(sheet_num, xls_name, newworkbook):
    pass
    # newworksheet = newworkbook.get_sheet(sheet_num)
    # # 获取表的有效行数
    # nrows = oldWorkbook.sheets()[sheet_num].nrows
    # for nrow in range(3, nrows):
    #     # 写入
    #     if nrow <=102:
    #         newworksheet.write(nrow, 0, xls_name + '_job' + str(nrow - 3).zfill(3), cell_style())
    #     newworksheet.write(nrow, 1, xls_name, cell_style())

# 表七
def sheet7(sheet_num, xls_name, newworkbook):
    newworksheet = newworkbook.get_sheet(sheet_num)
    # 获取表的有效行数
    nrows = oldWorkbook.sheets()[sheet_num].nrows
    str_list = xls_name.split("_")
    # app1
    if str_list[0] == "app1":
        newworksheet.write(113, 0, "开始", cell_style())
        newworksheet.write(114, 0, "结束", cell_style())
        for nrow in range(3, nrows):
            # 写入
            if nrow <= 102:
                newworksheet.write(nrow, 0, xls_name + '_job' + str(nrow - 3).zfill(3), cell_style())
            elif 103 <= nrow <= 112:
                # xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str((nrow - 100) * 10 - 21).zfill(3)
                # newworksheet.write(nrow, 0, "", cell_style())
                xls_name1 = xls_name + "_value" + str((nrow - 100) * 10 - 21).zfill(3)
                newworksheet.write(nrow, 0, xls_name1, cell_style())
            elif 113 <= nrow <= 114:
                pass
            else:
                for i in range(14):
                    newworksheet.write(nrow, i, "", cell_style())
            if nrow <= 114:
                newworksheet.write(nrow, 1, xls_name, cell_style())
            else:
                newworksheet.write(nrow, 1, "", cell_style())

    # app5
    elif str_list[0] == "app5":
        for nrow in range(3, nrows):
            # 写入
            newworksheet.write(113, 0, "开始", cell_style())
            newworksheet.write(114, 0, "结束", cell_style())
            if nrow <= 102:
                newworksheet.write(nrow, 0, xls_name + '_job' + str(nrow - 3).zfill(3), cell_style())
            elif 103 <= nrow <= 112:
                xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str(
                    (nrow - 100) * 10 - 21).zfill(3)
                newworksheet.write(nrow, 0, xls_name1, cell_style())
            elif 113 <= nrow <= 114:
                # xls_name1 = xls_name + "_value" + str((nrow - 110) * 10 - 21).zfill(3)
                pass
            else:
                for i in range(14):
                    newworksheet.write(nrow, i, "", cell_style())
            if nrow <= 114:
                newworksheet.write(nrow, 1, xls_name, cell_style())
            else:
                newworksheet.write(nrow, 1, "", cell_style())

    # app2~app4
    else:
        for nrow in range(3, nrows):
            # 写入
            if nrow <= 102:
                newworksheet.write(nrow, 0, xls_name + '_job' + str(nrow - 3).zfill(3), cell_style())
            elif 103 <= nrow <= 112:
                xls_name1 = "app" + str(int(str_list[0][3]) - 1) + "_" + str_list[1] + "_value" + str((nrow - 100) * 10 - 21).zfill(3)
                newworksheet.write(nrow, 0, xls_name1, cell_style())
            elif 113 <= nrow <= 122:
                xls_name1 = xls_name + "_value" + str((nrow - 110) * 10 - 21).zfill(3)
                newworksheet.write(nrow, 0, xls_name1, cell_style())

            newworksheet.write(nrow, 1, xls_name, cell_style())

# 表八
def sheet8(sheet_num, xls_name, newworkbook):
    newworksheet = newworkbook.get_sheet(sheet_num)
    # 获取表的有效行数
    nrows = oldWorkbook.sheets()[sheet_num].nrows

    newworksheet.write(3, 1, xls_name, cell_style())
    newworksheet.write(4, 1, xls_name, cell_style())

# 修改文件内容
def modify_file_content(sheet_num, xls_name, newworkbook):
    # 修改第一个表和第二个表
    if sheet_num == 0 or sheet_num == 1:
        sheet1(sheet_num, xls_name, newworkbook)
    # 修改第三个表
    elif sheet_num == 2:
        sheet3(sheet_num, xls_name, newworkbook)
    # 第四个表
    elif sheet_num == 3:
        sheet4(sheet_num, xls_name, newworkbook)
    # 第五个表
    elif sheet_num == 4:
        sheet5(sheet_num, xls_name, newworkbook)
    # 第六个表
    elif sheet_num == 5:
        sheet7(sheet_num, xls_name, newworkbook)
    # 第七个表
    elif sheet_num == 6:
        sheet8(sheet_num, xls_name, newworkbook)
    # 第8个表
    elif sheet_num == 7:
        pass
        # sheet8(sheet_num, xls_name, newworkbook)

# 边框样式
def cell_style():
    # 创建边框样式
    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    # DASHED虚线
    # NO_LINE没有
    # THIN实线
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    # 颜色
    # borders.left_colour = 0x40
    # borders.right_colour = 0x40
    # borders.top_colour = 0x40
    # borders.bottom_colour = 0x40
    # 初始化单元格样式
    style = xlwt.XFStyle()
    # 添加边框样式
    style.borders = borders
    return style

# 删除行
def del_nrow(newworksheet, nrow, ncols):
    # 获取表的有效列数
    # for ncol in range(ncols):
    #     newworksheet.write(nrow, ncol, "", cell_style())
    pass

def main(i, j):
    # 创建5000个xls文件
    xls_name = "app" + str(i+1) + "_wf" + str(j).zfill(5)
    copy_xls(xls_name)

if __name__ == '__main__':
    import time
    start = time.time()
    po = Pool(5)
    for i in range(5):
        for j in range(1000):
            po.apply_async(main, args=(i, j))
    print("进程开始！！！")
    po.close()
    po.join()
    print("进程结束！！！")

    end = time.time()
    print('Running time: %s Seconds'%(end-start))
