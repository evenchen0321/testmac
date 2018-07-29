#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

f = open("yesterday",'r',encoding="utf-8")
'''
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
笨办法
'''
'''
for i in range(5):
    print(f.readline())
第二种办法
'''

'''
for index,i in enumerate(f.readlines()):
    print(index,i.strip())
    if index == 9:
        print("----------------------")
        break
处理大数据不合适，太占内存
'''

count =0
for i in f:
    if count ==9:
        print("--------------")
        break
    count +=1
    print(count,i.strip())
#迭代器


f.close()