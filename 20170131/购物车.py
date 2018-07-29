#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

set = False    # 设置set 当输入为q就可以退出
file = open('购物车用户信息存档','r+',encoding='utf-8')    # 读取购物车用户信息文件
f = str(file.read())    # 将文件内容转化成字符串
for line in f:    # 逐行读取
    file_str = str(f)
data= eval(file_str)    # 将字符串转换为字典data
name = input("请输入姓名：")    # 提示输入用户名
password = input("请输入密码：")    # 提示输入密码
while True:
    if name in data:    # 用户名在字典data
        if password in data[name]:    # 密码如果能对应用户名，就欢迎登录
            salay = float(data[name][password])
            print('''\033[32;1m欢迎登录，当前余额为%s\033[0m'''%salay)
            break
        else:    # 否则密码输入错误，提示重新输入
            password = input("密码输入错误，请重新输入：")
            continue
    else:    # 否则判断为首次登录，将用户名，密码，工资存到用户信息文件中
        password_salay = {}
        salay_str = input("欢迎首次登录，请输入你的工资：")    # 输入工资数
        salay = float(salay_str)    # 将输入的字符串转换为数字
        password_salay[password] = salay    # 将工资对应到密码
        data[name] = password_salay    # 将密码-工资对对应到用户名
        file.seek(0)    # 文件的读取移到开头
        file.write(str(data))    # 写入新的字典信息
        file.tell()    # 返回当前位置
        break


list = [    # 购物清单
    ["iphone",5800],
    ["bike",800],
    ["macbook",17500],
    ["book",75],
    ["apple",5]
]

file_list_r = open('历史购买记录','r+',encoding='utf-8')    # 读取历史购买记录文件
f_list_r = str(file_list_r.read())
shoppinglist_dict = eval(f_list_r)    # 将历史记录信息转换为字典
if name not in shoppinglist_dict:    # 如果首次登录，会没有历史记录
    shoppinglist_dict[name] = []    # 首次登录历史记录留空
shoppinglist = shoppinglist_dict[name]    # 不是首次登录，将之前历史记录赋值到变量
shoppinglist_now = []    # 本次购物记录留空
choose = input("\n是否需要查询历史购物记录（y/n）:")    # 询问是否需要查询历史记录
if choose == 'y':    # 选y，输出历史购物记录
    print("\n\n-----------历史购物记录------------")
    print(shoppinglist)
    print("--------------结束---------------\n\n")

while not set:    # 购物车开始
    print('-----------商品清单------------')    # 输出商品清单
    for index,item in enumerate(list,1):
        print(index,item)
    print("-------------结束--------------")
    number = input("请输入想购买的商品编号：")    # 输入商品编号
    if number == "q":    # 当输入为q，退出，打印本次购物清单
        set = True
        data[name][password] = str(salay)    # 将字符串的工资给到对应用户名下的密码-工资对中
        file.seek(0)
        file.write(str(data))    # 将用户信息写入购物车用户信息存档中
        file.tell()
        print("------------购物清单------------")    # 打印购物清单，提示余额
        print(shoppinglist_now)
        print("您的余额为：",salay)
        print("-------------结束--------------")
        shoppinglist.extend(shoppinglist_now)    # 将本次购物记录追加到购物记录列表中
        shoppinglist_dict[name] = shoppinglist    # 购物列表与用户名做对应
        file_list_r.seek(0)
        file_list_r.write(str(shoppinglist_dict))    # 写入字符串的购物历史记录
        file_list_r.tell()
    elif number.isdigit() == False:    # 校验输入是否为整数
        print("\033[31;1m输入不是编号内容，请重新输入\033[0m")
    elif int(number)>int(len(list)) or int(number)<= 0:    # 如果输入值不在清单中，提示报错
        print("\033[31;1m您所购买的商品不在清单中\033[0m")
    else:
        number_buy = int(number)-1
        if list[number_buy][1]<(salay):    # 如果余额够，提示成功购买，显示余额
            salay = salay - int(list[number_buy][1])
            msg = '''
                            \033[32;1m您已将%s加入购物车中
                            余额为%s\033[0m
                            ''' % (list[number_buy][0],salay)
            print(salay)
            print(msg)
            shoppinglist_now.append(list[number_buy])    # 本次购物信息加到本次购买记录中
        else:
            print("\033[31;1m您已没有余额可以购买\033[0m")    # 否则提示余额不足





