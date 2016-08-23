# step5.py
# ----------
# Challenge: The API will again give you a dictionary. The value for datestamp
# is a string, formatted as an ISO 8601 datestamp. The value for interval is
# a number of seconds.

# Implementation
import requests
import json
import datetime 


# Fire initial HTTP POST to API
url ='http://challenge.code2040.org/api/dating'
init_json = {"token" : "c7ab03d52031cf3b84510fdae8af5689"}
r = requests.post(url, data=init_json)

# Convert response to dictionary
d = r.content
dictionary = json.loads(d)
datestamp = dictionary["datestamp"] 
interval =  dictionary["interval"]

# Convert from ISO8601 to datetime
start_date = datetime.datetime.strptime(str(datestamp), "%Y-%m-%dT%H:%M:%SZ")
# add interval
end_date = start_date + datetime.timedelta(seconds=interval)

# Convert back to ISO format the same way as original
date_time_val = end_date.isoformat() + 'Z'

# Send final value via HTTP POST
url2 = 'http://challenge.code2040.org/api/dating/validate'
final_json = {"token" : "c7ab03d52031cf3b84510fdae8af5689", "datestamp": date_time_val}
req = requests.post(url2, json=final_json)