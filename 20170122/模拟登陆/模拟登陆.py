#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even


count = 0  # 为了记录需求中3次输入错误避免的次数，计数项赋初始值
load = True  # 为了完成功能后退出，赋初始值
file = open("正确用户信息文件",'r',encoding='utf-8')  # 打开正确用户信息文档，获取正确的用户名密码
file_wrong = open("锁定用户信息文件",'r+',encoding='utf-8')  # 打开已锁定的用户信息文档，获取锁定的用户名密码
line = eval(file.readline())  # 将正确信息中的字符串转换成字典（原字符串为字典格式）
line_wrong = eval(file_wrong.readline())  # 将正确信息中的字符串转换成列表（原字符串为列表格式）


def out():  # 将重复代码定义，功能是帮助跳出while循环并关闭已打开文档
    global load  # 声明全局变量
    load = False  # 赋值load，为了跳出while循环
    file_wrong.close()  # 关闭正确用户信息文档
    file.close()  # 关闭锁定用户信息文档

while load:  # 判断是否已完成功能
    name = input("请输入用户名：")  # 输入用户名
    password = input("请输入密码：")  # 输入密码
    if name in line and name not in line_wrong:  # 判断用户名是否正确，和是否已被锁定
        while count <= 3:  # 判断是否已循环3次
            if password == line[name]:  # 判断用户名是否对应正确的密码
                print("您已成功登陆")  # 输出成功登陆信息
                out()  # 调用自定义out方法
                break  # 跳出本次循环
            else:  # 说明未输入正确的密码
                count +=1  # 计数项自加一
                msg_count = '''\033[31;0m第%s次密码输入错误\033[1m\n'''%(count)  # 提示输入错误次数
                print(msg_count)  # 打印错误次数信息
                if count < 3:  # 小于三次错误输入，可以重新输入
                    password = input("密码错误，请重新输入密码：")  # 重新输入密码
                elif count == 3:  # 判断是否已输错三次
                    print("已输错3次，账号已锁定")  # 打印锁定提示信息
                    line_wrong.append(name)  # 将已锁定信息加入锁定元组中
                    file_wrong.seek(0)  # 输入指针移到开头，如果不移动会产生多个元组
                    file_wrong.write(str(line_wrong))  # 写入锁定信息
                    file_wrong.tell()  # 获取当前的输入指针位置，如果不获取会产生多个元组
                    out()  # 调用out方法
                    break
    elif name in line_wrong:  # 判断用户名是否在已锁定用户名中
        print("该用户名已被锁定")  # 打印已锁定通知信息
        out()  # 调用自定义out方法
        break  # 跳出当前循环
    else:  # 说明用户名不在正确用户名信息中
        print("该用户名不存在")  # 打印用户名输入错误信息
        out()  # 调用out方法


