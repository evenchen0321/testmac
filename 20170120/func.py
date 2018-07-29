#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

# def test():
#     print("in the testing....")
#     return 10
#
# x = test()
# print(x)

# def test(x,y,z=2):
#     print(x)
#     print(y)
#     print(z)
#
# test(1,2,z=4)
#
# def test1(*args): #实参不确定，使用这种
#     print(args)
#
#
# test1(1,2,3)
# test1(*[4,5,6])
#
# def test2(**kwargs): #字典传输，把关键字参数转换成字典式的键值对方式
#     print(kwargs)
#
# test2(name='cx',age='8',sex='male')
# test2(**{'name':'cx','age':'8','sex':'male'})

def test4(name,age,*args,**kwargs): #*args 通过位置参数传入
    print(name)
    print(age)
    print(args)
    print(kwargs)


test4('cx',34 ,56,name2='123',name3='dfg')