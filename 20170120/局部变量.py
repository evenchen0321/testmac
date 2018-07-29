#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

def change_name(name):
    print("before",name)
    name = "CHENXU"  #此为局部变量，只作用于这个函数作为作用域
    print("after",name)

name ='cx'
change_name(name)
print(name)