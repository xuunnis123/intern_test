# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:33:20 2019

@author: Ji-Yang Lin
"""

import requests
import json
import cgi,os
import cgitb;cgitb.enable()
global r

r=requests.get('https://ssl.logink.org/authapi/rest/auth/apply?userid=26088&password=a12345678&resource=493CA712371E0188E053C0A87F0C0188')
page=requests.get("https://xuunnis123.github.io/intern_test/index.html")

save=(r.json())
print(save)
if save['resultCode']==100000:
    getToken=save['token']
    print(getToken)
else :
    r=requests.get('https://ssl.logink.org/authapi/rest/auth/apply?userid=26088&password=a12345678&resource=493CA712371E0188E053C0A87F0C0188')
    

form =cgi.FieldStorage()
print(page.json())