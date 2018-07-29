#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even
陈旭的年龄 =26
count = 0
'''
while True:
    if count ==3:
        break
    cx = int(input("cx:"))
    if cx == 陈旭的年龄:
        print("yes,you got it!")
        break
    elif cx > 陈旭的年龄:
        print("think smaller")
    else:
        print("think bigger")
    count =count+1
'''
while count <3:
    cx = int(input("cx:"))
    if cx == 陈旭的年龄:
        print("yes,you got it!")
        break
    elif cx > 陈旭的年龄:
        print("think smaller")
    else:
        print("think bigger")
    count +=1
else:
    print("over!")

