#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

Buy_success = []
Salay =input("请输入工资：")
Money_rest = int(Salay)
List =[
       ['iphone',5800],
       ['mac pro',12000],
       ['starbuck lattle',35],
       ['book',81],
       ['bike',800]
       ]
# print("1.",List[0][0],List[0][1])
# print("2.",List[1][0],List[1][1])
# print("3.",List[2][0],List[2][1])
# print("4.",List[3][0],List[3][1])
# print("5.",List[4][0],List[4][1])

while True:
    for index,item in enumerate(List):
        print(index+1,item)
    break

while input() != "q":
    Buy_number = int(input("请输入商品编号:")) - 1
    if Buy_number >=int(len(List)) and Buy_number <0:
        print("你输入的错误的商品编号，请重新输入")
        Buy_number = int(input("请输入商品编号:")) - 1
    else:
        Buy_object = List[Buy_number][0]
        msg = 'adding %s to your shopping cart' % (Buy_object)
        Money_test = Money_rest - int(List[Buy_number][1])
        print(msg)
        while True:
            if Money_test < 0:
                print("But you have not enough moeny,you can't buy it")
                break
            else:
                Money_rest = Money_test
                Buy_success.append(List[Buy_number])
                print("余额为：", Money_rest)
                break

            print("余额为：", Money_rest)


else:
    print("你已购买：")
    print(Buy_success)
    print("你的余额为：",Money_rest)





# you have bought below:

# your balance: