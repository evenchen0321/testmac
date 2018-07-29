#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

salay = int(input("请输入你的工资："))
list = [
    ["iphone",5800],
    ["bike",800],
    ["macbook",17500],
    ["book",75],
    ["apple",5]
]
shoppinglist=[]

while True:
    for index,item in enumerate(list):
        print(index,item)
    number = input("请输入想购买的商品编号：")
    if int(number) >= int(len(list)) and int(number)< 0:
        print("您所购买的商品不在清单中")
    elif number == "q":
        print("-----shopping list------")
        for i in shoppinglist:
            print(i)
            print("你的余额为：",salay)
            break
    else:
        if list[int(number)][1]<(salay):
            salay = salay - int(list[int(number)][1])
            msg = '''
                            您已将%s加入购物车中
                            余额为%d
                            ''' % (list[int(number)][0],salay)
            print(msg)
            shoppinglist.append(list[int(number)])
        else:
            print("已没有余额可以购买")






