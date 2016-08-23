# #apiChallenge.py

import requests
import json
url ='http://challenge.code2040.org/api/register'
js = {"token" : "c7ab03d52031cf3b84510fdae8af5689", "github" : "https://github.com/yadelab/API_challenge.git"}

r = requests.post(url, data=js)
print(r.response)
print(r.content)
def stringReverse(str_input):
  reversed_str = ""
  for string in str_input:
    reversed_str= string + reversed_str
  return reversed_str

