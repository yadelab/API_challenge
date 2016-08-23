# step3.py
# -------
# Challenge: Locate the needle in the haystack array. You are going to send
# back the position, or index, of the needle string. The API expects indexes
# to start counting at 0.

# Implementation
import requests
import json
__author__ = "Yadel Abraham"


# Fire initial HTTP POST request to API
url ='http://challenge.code2040.org/api/haystack'
init_json = {"token" : "c7ab03d52031cf3b84510fdae8af5689"}
r = requests.post(url, data=init_json)
#convert response to dictionary
dictionary = r.content #dict contains needle & haystack
d = json.loads(dictionary)
needle = d["needle"] #string
haystack_arr = d["haystack"] #array

# Helper to find the 'needle' in the array
def findNeedle(_arr):
	""" Takes in the haystack and finds the position of the needle string if 
		needle is in the array

	:param _arr: the haystack array
	:return: The position, or "index"
	"""

	if needle not in _arr:
		return None
	index = 0
	for haystack in haystack_arr:
		if haystack == needle:
			return index
		index+=1

# Send index of needle via HTTP POST
index =  str(findNeedle(haystack_arr)) #convert back to string
url2 ='http://challenge.code2040.org/api/haystack/validate'
final_json = {"token" : "c7ab03d52031cf3b84510fdae8af5689", "needle" : index}
req = requests.post(url2, data=final_json)