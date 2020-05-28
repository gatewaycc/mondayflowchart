# Run 'pip install requests' in CMD

import requests
import json

apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjQ1NzQ0NzA1LCJ1aWQiOjEyODI1OTM2LCJpYWQiOiIyMDIwLTA1LTE5VDE5OjA0OjI1LjAwMFoiLCJwZXIiOiJtZTp3cml0ZSJ9.C76pJ4PMUnnFy_vM09MwwnENohxhRMhA56TmLJ7p-lE"
apiURL = "https://api.monday.com/v2"
headers = {"Authorization" : apiKey}

# Variables to know:
### Facilities Board ID: 475894573
### AVP/Dean
### VP
### Project Manager

########################################################

# Request query of AVP/Dean data

# figure out how to reverse the order of items being called or how to call the latest submission via creation log
query = '{boards (ids:475894573){ items(limit: 1) {column_values(ids:avp_dean) {text}}}}'
data = { 'query' : query}

r = requests.post(url=apiURL, json=data, headers=headers)
print(r.json())

# Assign AVP/Dean variable

