#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even


import requests,base64,os


def token():
    api_url = "http://app.360scm.com/SCM.TMS7.WebApi/Oauth/GetTokenByCustomer"
    apikey_eo = {"apikey":"vlzSxLhLi51N0zOaOy4y2je0kXi+eTS4Cz5FLww9a0ospphLXhqPCeMiOHU+uIZL9MJ79A5N+02IfTPmviiUE57Ze9lDgvDbS1puOM7R9YkSAVMvvUE9WFnQ7YxIaS/1A25I+YO52397P4cUB4eqvTaeuvMdw7H1t3/WuTF54RHfBN8ufZdIDb9CRRudb6GV6yfzEG0Vcm5mwH7KVVBvf5uyXnsylU6yjAg2K2St3tk="}
    r = requests.get(api_url,params=apikey_eo)
    token_value = r.json()["token"]
    print(token_value)
    return token_value


def getPodFiles():
    api_url = "http://app.360scm.com/SCM.TMS7.WebApi/Customer/GetPodFiles"
    token_value = token()
    gid_num = input("请输入查询单号：")
    pragm = {"token":token_value,"gid":gid_num,"typeCode":2}
    r = requests.get(api_url,params=pragm)
    filedata = r.json()["data"][0]["FileList"][0]["FileData"]
    filename = r.json()["data"][0]["FileList"][0]["FileName"]
    r = base64.b64decode(filedata)
    os.chdir("pod_photo")
    print(os.getcwd())
    with open(filename,"wb") as f:
        f.write(r)



getPodFiles()