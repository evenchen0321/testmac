#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

menu = {
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

level = []
while True:
    for key in menu:
        print(key)
    choose = input("choose:").strip()
    if choose == "b":
        if len(level) == 0:break
        menu = level[-1]
        level.pop()

    if choose not in menu:continue
    level.append(menu)
    menu = menu[choose]