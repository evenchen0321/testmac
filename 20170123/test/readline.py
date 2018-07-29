#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

f = open("readline",'r',encoding="utf-8")
f1 = f.read()
for line in f1:
    f_str = f1
print("第一次打印")
print(f_str)
f.close()

g = open("readline",'r',encoding="utf-8")
for line in g:
    g_str = g.read()
print("第二次打印")
print(g_str)
g.close()