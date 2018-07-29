#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

# a = 4
# print(a)
# a = 5
# print(a)
# b = 4

# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# print(tu[0])
# print(tu[1][2]["k1"])
# tu[1][2]["k2"].append("123")
# print(tu)
# n = 0
# while True:
#     if n<50:
#         i =2*n+1
#         print(i)
#         n += 1


# s = "你是风儿%%%%我是沙%s"
# n = s %('僧')
# print(n)

# 使用while循环实现输出2 - 3 + 4 - 5 + 6 ... + 100 的和

def n1():
    n = 2
    a = 2
    while n<51:
        i = 2*n
        # print(i)
        a += i
        n += 1
    return a


def n2():
    n = 1
    b = 0
    while n<50:
        i1 = 2*n+1
        # print(i1)
        b += i1
        n += 1
    return b


print(n1()-n2())


# 1*1 = 1
# 1*2 = 2 2*2 = 4