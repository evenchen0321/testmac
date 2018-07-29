#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

# a = '''"it"'''
# print(a)
# a = a.strip('"')
# print(a)
# # print(a[2])
#
# select  * from staff_table where enroll_date like "2015"

# k = {"1","2","3"}
# for i in k:
#     b = i.count()
# print(b)

a = 'UPDATE staff_table SET dept = "Market" WHERE where dept = "IT"'
a = a.split()
print(a)