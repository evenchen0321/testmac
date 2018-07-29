#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

import shutil,os,time,sys

# f1 = open("模块学习random.py")
# f2 = open("模块学习random_shutiltest.py","w")
# shutil.copyfileobj(f1,f2)

# shutil.copy("/Users/chenxu/PycharmProjects/test/20170201/readme","copytest")

print(os.stat("/Users/chenxu/PycharmProjects/test/20170201/readme"))
a = os.stat("/Users/chenxu/PycharmProjects/test/20170201/readme")
print(time.strftime("%Y-%m-%d",time.gmtime(a.st_atime)))
print(time.gmtime(a.st_atime))

# shutil.make_archive("/Users/chenxu/PycharmProjects/test",format="zip",root_dir="/Users/chenxu/PycharmProjects/test/20170507")

print(sys.path)

