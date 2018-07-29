#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

for i in range(10):
    if i <5:
        continue
    print(i)

name = [1,2,3,4,5,6,7,8,9]
print(name[-5:3])
name.reverse()
print(name)