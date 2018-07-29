#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

import sys

file = open("三级菜单文本内容",'r',encoding='utf-8')    # 打开3级菜单文本文件
f = file.read()
for line in f:    # 读取文件中每行信息
    file_str = str(f)    # 将每行信息转成字符串格式
data = eval(file_str)    # 字符串转成字典格式


def list():    # 定义读取字典中的key，即第一层内容展示
    for i in data:
        print(i)


def choose1(choice1):    # 定义第一层选择
    while choice1 != 'q':    # 输入为q即退出程序
        global one
        one = choice1    # 定义全局变量one 使得其他函数可以调用
        if choice1 in data:
            for i2 in data[one]:
                print("\t", i2)    # 展示3级菜单中所选第一层下的第二层信息
            choose2(input("请输入第二层："))    # 调用choose2函数，输入第二层信息
            break
        elif choice1 == 'b':    # 输入b退出循环
            break
        else:
            error = input("输入错误，请重新输入第一层：")    # 输入内容不在第一层选项中
            if error == 'q':    # 输入q退出程序
                sys.exit()
            else:   # 否则调用本函数
                choose1(error)
    else:
        sys.exit()


def choose2(choice2):   # 定义第二层选择
    while choice2 != 'q':
        global two
        two = choice2   # 定义全局变量two 使得其他函数可以调用
        if choice2 in data[one]:
            for i3 in data[one][two]:
                print("\t\t", i3)   # 展示3级菜单中所选第二层下的第三层信息
            choose3(input("请输入第三层："))    # 调用choose3函数，输入第三层信息
            break
        elif choice2 == 'b':    # 输入b退回第一层
            list()  # 调用list函数展示第一层信息
            choose1(input("请输入第一层："))
            break
        else:
            error2 = input("输入错误，请重新输入第二层：")    # 输入错误，重新输入
            if error2 == 'q':    # 输入q退出程序
                sys.exit()
            else:
                choose2(error2)    # 调用本函数
    else:
        sys.exit()


def choose3(choice3):   # 定义第三层选择
    while choice3 != 'q':
        global three
        three = choice3    # 定义全局变量three 使得其他函数可以调用
        if choice3 in data[one][two]:
            for i4 in data[one][two][three]:
                print("\t\t\t", i4)    # 展示3级菜单中所选第三层下的第四层信息
            choose4(input("\033[31;1m最后一层，退回上一层请按‘b’，退出请按'q'\033[0m"))    # 调用choose4函数，提示退出或退回
            break
        elif choice3 == 'b':    # 输入为b退出
            choose1(one)
            break
        else:
            error3 = input("输入错误，请重新输入第三层：")    # 输入错误，可以重新输入，q退出
            if error3 == 'q':
                sys.exit()
            else:
                choose3(error3)    # 调用本函数
    else:
        sys.exit()


def choose4(choice4):   # 定义最后退出
    while choice4 != 'q':   # 输入q退出
        if choice4 == 'b':  # 输入b退回上一层
            choose2(two)
        else:
            choose4(input("\033[41;1m真的是最后一层了，退回上一层请按‘b’，退出请按'q'\033[0m"))   # 声明结束
    else:
        sys.exit()


print("退出请按'q'，返回上级菜单请按'b'")    # 声明功能
list()  # 调用list函数展示第一层信息
choose1(input("请输入第一层："))   # 主程序，开始运行





