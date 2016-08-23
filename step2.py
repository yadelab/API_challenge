# step2.py
# ----------
# Challenge: This endpoint will return a string that your code should
# then reverse. Once that string is reversed, send it back to us

# Implementation
import requests
import json
__author__ = "Yadel Abraham"


# Fire initial HTTP POST request to API
url ='http://challenge.code2040.org/api/reverse'
init_json = {"token" : "c7ab03d52031cf3b84510fdae8af5689"}
r = requests.post(url, data=init_json)
# String from response
str_ = r.content

# Helper method to reverse a string
def stringReverse(str_input):
	""" Reverses string from the API response

	:param _str_input: A string from the API
	:return: Reversed string 	
	"""
	reversed_str = ""
	for string in str_input:
		reversed_str= string + reversed_str
	return reversed_str

# POST the reversed string to API
rev = stringReverse(str_)
url2 = 'http://challenge.code2040.org/api/reverse/validate'
final_json = {"token" : "c7ab03d52031cf3b84510fdae8af5689", "string" : rev}
req = requests.post(url2, data=final_json)