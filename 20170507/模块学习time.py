#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

import time,datetime

print(time.altzone/3600)
print(time.asctime())
print(time.localtime())
print(type(time.localtime()))
t = time.localtime()
print(t.tm_mon)
print(time.ctime())
print(time.gmtime(time.time()-time.altzone))
print(time.mktime(time.localtime())/(3600*365*24))
print(datetime.datetime.now())
test = 45
print(datetime.datetime.now().replace(minute=test))