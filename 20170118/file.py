#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

f = open("yesterday",'a',encoding="utf-8")
#print(f.read())  r模式下
#f.write("i am even") w模式下
f.write("678")   a模式下
f.close()