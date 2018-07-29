#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

data = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":{"CICC","HP"},
            "东直门":{"Advent","飞信"},
        },
        "海淀":{},
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{},
    },
}
exit_falg = False

while not exit_falg:
    for i in data:
        print(i)
    choice = input("请输入：")
    if choice in data:
        while not exit_falg:
            for i2 in data[choice]:
                print("\t", i2)
            choice2 = input("请输入：")
            if choice2 in data[choice]:
                while not exit_falg:
                    for i3 in data[choice][choice2]:
                        print("\t\t",i3)
                    choice3 = input("请输入：")
                    if choice3 in data[choice][choice2]:
                        while not exit_falg:
                            for i4 in data[choice][choice2][choice3]:
                                print("\t\t\t",i4)
                            choice4 = input("最后一层，退出请按‘b’")
                            if choice4 == "b":
                                break
                            elif choice4 == "q":
                                exit_falg = True
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_falg = True
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_falg = True













