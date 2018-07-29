#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even


def exit():
    while True:
        b_input = input("查询完毕退出请按'b'：")
        if b_input == 'b':
            flag_exit_f = 'out'
            return flag_exit_f
        else:
            return exit()


print(exit())