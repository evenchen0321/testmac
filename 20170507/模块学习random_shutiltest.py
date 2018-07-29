#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

import string,random

print(string.ascii_letters + string.digits)
a = string.ascii_letters + string.digits
print("".join(random.sample(a,6)))

print(random.randint(1,6))
print(random.randrange(1,3))

checkcode = ""
for i in range(4):
    current = random.randrange(0,4)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print(checkcode)