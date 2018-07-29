#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

def foo(s):
    print(s)
    while int(s)  > 0:
        print(s)
        if int(s) == 1:
            print("已等于1")
            break
        else:
            foo(input("sss:>>>"))

foo(2)