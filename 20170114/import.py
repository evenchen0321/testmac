#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

'''
import sys
print(sys.path)
print(sys.argv)
print(sys.argv[3])
'''

import os
#cmd_ans = os.system("dir")
cmd_ans1 = os.popen("dir").read()
#print(cmd_ans)
#print("1-->",cmd_ans1,cmd_ans)
print("2-->",cmd_ans1)


