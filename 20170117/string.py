#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even
name = "My name is Even"

print(name.capitalize()) #首字母大写
print(name.count("e")) #计算字符数量
print(name.center(50,'-')) #把字符居中
print(name.endswith("en")) #判断是否是对应字符结尾
print(name.expandtabs(tabsize=0)) #将tab键转换为空格
print(name.find("name")) #返回字符的位置，可以用于切片
print(name[name.find("name"):7]) #字符切片

name = "My name is {name},i am {year} old"
print(name.format(name="Even",year="25"))
print(name.format_map( {'name':'Even','year':'25'} ))
print("ab123".isalnum()) #是否包含英文和数字，特殊字符除外
print("1A".isdecimal()) #是否是十进制
print("123.1".isdigit()) #是否整数
print("a和我1q".isidentifier()) #是否合法用户名
print("33.33".isnumeric()) #是否数值型的,不包含小数
print("My Name Is".istitle()) #是否全部首字母大写
print("abc".isprintable()) #是否可打印的
print("My Name Is".isupper()) #是否是大写

print('+'.join(['1','2','3']))
print(name.ljust(50,"1")) #设置长度是50，否则最后以字符补全
print(name.rjust(50,"2")) #设置长度是50，否则最前以字符补全
print("EVEN".lower()) #大写转小写
print("even".upper()) #小写转大写
print("\nEven".lstrip()) #左边去除空格
print("\nEven\n".rstrip()) #右边去除空格
print("    Even\n".strip()) #去除所有空格
print("---")

table = str.maketrans("abcdefg","1234567")
print("back up".translate(table))

print("Aeven".replace('e','E',1))
print('Alex li'.rfind('l')) #返回最右边的字符位置
print("a+b+c".split('+')) #以字符分隔列表
print("EVen Chen".swapcase()) #小写转大写，大写转小写

