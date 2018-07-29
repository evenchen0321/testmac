#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even


import sys


def dict_file():    # 将文本输出为字典
    dict = {}
    dict_all = {}
    with open("员工信息存档", 'r', encoding='utf-8') as f:    # 逐行读取员工信息并转化为字典
        for line in f:
            line = eval(str(line.strip().split(",")))
            dict['staff_id'] = str(line[0])
            dict['name'] = line[1]
            dict['age'] = line[2]
            dict['phone'] = line[3]
            dict['dept'] = line[4]
            dict['enroll_date'] = line[5]
            dict_all[line[3]] = dict.copy()    # 此处必须用copy，否则输出只对应最后一行的值
    return dict_all    # 返回存有员工信息的字典


def file_dict(dict_all):    # 将字典输出到文本
    with open("员工信息存档",'w',encoding='utf-8') as f:    # 打开信息存档并格式化写入字典对应字段的值
        for k, v in dict_all.items():
            v = v.copy()
            file = "%s,%s,%s,%s,%s,%s\n" % (v['staff_id'], v['name'], v['age'], v['phone'], v['dept'], v['enroll_date'])
            f.write(file)


def action_list():    # 显示操作列表和编号，并返回操作编号
    print("-------------------------------------------------")
    print("\t\t\t\t欢迎来到员工信息表")
    print("-------------------------------------------------")
    print("操作清单如下：")
    print('''
    1.查询
    2.添加
    3.修改
    4.删除
    5.退出
    ''')
    print("-------------------------------------------------")
    action_num = numif(input("请输入需要操作的编号：（请输入数字）"))
    return action_num    # 返回操作的编号


def numif(number_input): # 判断输入是否为数字
    while not number_input.isdigit():    # 输入不是数字就进入循环
        number_input = input('\033[31m 输入%s不是数字，请重新输入!\033[0m' % number_input)    # 提示重新输入
    number = number_input
    return number    # 返回数字


def employee_exit():    # 定义退出功能
    flag_exit = True
    b_input = input("操作完毕退出请按'b'：")
    while flag_exit:
        if b_input == 'b':
            flag_exit = False
            return flag_exit

        else:
            return employee_exit()   # 使用尾递归，而不需要递归一层层退出


def inquiry():    # 查询功能
    dict_all = dict_file()
    grammar = input("请输入语法：")
    grammar_list = grammar.split()
    if grammar == "select name,age from staff_table where age > %s" % grammar_list[7]:
        count = 0
        print("查询结果如下：")
        for k,v in dict_all.items():
            if v["age"] > grammar_list[7]:
                print(v["name"],v["age"])
                count += 1
        print("\033[32m共查询到%s条记录\033[0m"%count)

    elif grammar == "select  * from staff_table where dept = %s" % grammar_list[7]:
        count = 0
        print("查询结果如下：")
        for k, v in dict_all.items():
            grammar_list[7] = grammar_list[7].strip('"')
            if grammar_list[7] == v["dept"]:
                print(v['staff_id'], v['name'], v['age'], v['phone'], v['dept'], v['enroll_date'])
                count += 1
        print("\033[32m共查询到%s条记录\033[0m" % count)

    elif grammar == 'select  * from staff_table where enroll_date like %s' % grammar_list[7]:
        count = 0
        print("查询结果如下：")
        for k, v in dict_all.items():
            grammar_list[7] = grammar_list[7].strip('"')
            if grammar_list[7] in v["enroll_date"]:
                print(v['staff_id'], v['name'], v['age'], v['phone'], v['dept'], v['enroll_date'])
                count += 1
        print("\033[32m共查询到%s条记录\033[0m" % count)

    else:
        print("所查语法不存在，请退出重新查询")


def add():
    dict = {}
    dict_all = dict_file()
    print("\033[32m请按提示输入对应信息：\033[0m")
    i = 0
    for k,v in dict_all.items():    # 获取最后一个员工编号
        i = v['staff_id']
    dict['staff_id'] = str(int(i)+1)    # 自动新增编号加一
    dict['name'] = input("请输入新增人员姓名：")
    dict['age'] = input("请输入新增人员年龄：")
    dict['phone'] = input("请输入新增人员手机号：")
    dict['dept'] = input("请输入新增人员所属部门：")
    dict['enroll_date'] = input("请输入新增人员入职日期：")
    dict_all[dict['phone']] = dict
    file_dict(dict_all)


def delete():
    dict_all = dict_file()
    print("人员信息如下：")
    for k, v in dict_all.items():
        v = v.copy()
        print("%s,%s,%s,%s,%s,%s" % (v['staff_id'], v['name'], v['age'], v['phone'], v['dept'], v['enroll_date']))
    del_num = input("请输入需要删除的员工编号：")
    for k,v in dict_all.items():
        if v['staff_id'] == del_num:
            k_del = k
    del dict_all[k_del]
    file_dict(dict_all)


def revise():
    dict_info = list_info()
    print(dict_info)
    dict_all = dict_file()
    grammar = input("请输入语法：")
    grammar_list = grammar.split()
    revise_info = grammar_list[3]
    info_old = str(grammar_list[5])
    info_new = str(grammar_list[9])
    update_old = grammar_list[5].strip('"')
    update_new = grammar_list[9].strip('"')
    info_list = dict_info[revise_info]
    if revise_info in dict_info:
        print(update_old)
        print(info_list)
        if update_old not in info_list:
            print("\033[需要修改的31m%s不存在！\033[0m" % info_old)

        elif grammar == 'UPDATE staff_table SET %s = %s WHERE %s = %s'% (revise_info,info_old,revise_info,info_new):
            count = 0
            for k,v in dict_all.items():
                if v[revise_info] == update_old:
                    v[revise_info] = update_new
                    count += 1
                    file_dict(dict_all)
                    print("\033[32m共修改到%s条记录\033[0m" % count)

        else:
            print("输入语法错误")
    else:
        print("\033[31m输入列名错误！\033[0m")


def list_info():
    dict_part = {}
    list_name = []
    list_age = []
    list_phone = []
    list_dept = []
    list_endate = []
    dict_all = dict_file()
    for k,v in dict_all.items():
        name = v['name']
        list_name.append(name)
        list_age.append(v['age'])
        list_phone.append(v['phone'])
        list_dept.append(v['dept'])
        list_endate.append(v['enroll_date'])
    dict_part['name'] = list_name
    dict_part['age'] = list_age
    dict_part['phone'] = list_phone
    dict_part['dept'] = list_dept
    dict_part['enroll_date'] = list_endate
    return dict_part


dict_key = ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date']
flag = True    # 主函数开始
while flag:
    flag_main = True
    flag_action = True
    action_num = action_list()    # 展示功能项，并输入操作编号
    while flag_main:
        if action_num == '1':
            inquiry()
            flag_main = employee_exit()
            break

        if action_num == '2':
            add()
            flag_main = employee_exit()
            break

        if action_num == '3':
            revise()
            flag_main = employee_exit()
            break

        if action_num == '4':
            delete()
            flag_main = employee_exit()
            break

        if action_num == '5':
            sys.exit()

        elif action_num not in range(5):    # 当输入不在编号中，提示并重新输入
            print("\033[31;1m输入错误请重新输入！\033[0m")
            flag_main = False