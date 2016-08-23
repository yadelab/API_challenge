# step4.py
# -------
# Challenge: Your job is to return an array containing only the strings that
# do not start with that prefix.

# Implementation
import requests
import json
__author__ = "Yadel Abraham"


# Fire initial HTTP POST request to API
url ='http://challenge.code2040.org/api/prefix'
init_json = {"token" : "c7ab03d52031cf3b84510fdae8af5689"}
r = requests.post(url, data=init_json)
#convert response to dictionary
d = r.content
dictionary = json.loads(d)
prefix = dictionary["prefix"] 
array =  dictionary["array"]

# Helper method to filter out words 
def filterPrefix(wordsArray, prefix):
	""" Takes in the list of words we get for the API response filters out those 
		containing the prefix and returns the rest

	:param wordsArray: List of all words from API
	:param prefix: The prefix string we're filtering for 
	:return: A new array of words that do not start with prefix 
	"""

	noPrefix = []	
	i = len(prefix)
	for word in wordsArray:
		if word[:i] != prefix:
			noPrefix.append(word)
		continue
	return noPrefix

# Send the filtered array back via HTTP POST
filteredArray = filterPrefix(array, prefix)
url2 ='http://challenge.code2040.org/api/prefix/validate'
final_json = {"token" : "c7ab03d52031cf3b84510fdae8af5689", "array" : filteredArray}
req = requests.post(url2, json=final_json)