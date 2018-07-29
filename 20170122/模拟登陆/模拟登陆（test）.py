#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even


Again = False
print("欢迎登陆**系统，默认首次登陆即为注册")
Right_file = open("正确用户信息文件",'r',encoding='utf-8')
Line = Right_file.readline()
Mode = int(input("首次登陆注册请输入“1”，已注册用户请按任意键"))
while Mode == 1:
    Line_dict = eval(Line)
    Right_name = input("请注册您的用户名：")
    Right_password = input("请注册您的密码：")
    while not Again:
        if Right_name in Line_dict:
            input_quit = input("已存在该用户名，请输入q重新录入")
            if input_quit == 'q':
                Again = True


        else:
            Msg_right = '''该用户名：%s已注册完成''' % (Right_name)
            print(Msg_right)
            Line_dict[Right_name] = Right_password
            Line = str(Line_dict)
            Right_file.writelines(Line)
        break
    break







# Name = input("请输入您的用户名：")
# Password = input("请输入您的密码：")
#
#
#
#
# print("欢迎登陆")
# print("已尝试三次，该用户已锁定")



