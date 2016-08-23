#step1.py

import requests
import json
__author__ = "Yadel Abraham"

#Registering my account
url ='http://challenge.code2040.org/api/register'
js = {"token" : "c7ab03d52031cf3b84510fdae8af5689", "github" : "https://github.com/yadelab/API_challenge.git"}
req = requests.post(url, data=js)