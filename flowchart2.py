# Quickstart Tutorial: https://support.monday.com/hc/en-us/articles/360013483119
# Run 'pip install requests' in CMD
# Run each test individually so as not to coincide with each other

import requests
import json

apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjQ1NzQ0NzA1LCJ1aWQiOjEyODI1OTM2LCJpYWQiOiIyMDIwLTA1LTE5VDE5OjA0OjI1LjAwMFoiLCJwZXIiOiJtZTp3cml0ZSJ9.C76pJ4PMUnnFy_vM09MwwnENohxhRMhA56TmLJ7p-lE"
apiURL = "https://api.monday.com/v2"
headers = {"Authorization" : apiKey}

######### test 1: request data #########
# query = ' { boards (limit: 5) {name id} }'
# data = { 'query' : query}

# r = requests.post(url=apiURL, json=data, headers=headers)
# print(r.json())

######### test 2: create new item #########
# query2 = 'mutation{ create_item (board_id:558120502, item_name:"WHAT IS UP MY FRIENDS!") { id } }'
# data = {'query' : query2}

# r = requests.post(url=apiURL, json=data, headers=headers) # make request
# print(r.json())

######### test 3: create new item with graphql variables #########
# query3 = 'mutation ($myItemName: String!) { create_item (board_id:558120502, item_name:$myItemName) { id } }'
# vars = {'myItemName' : 'Hello everyone!'}
# data = {'query' : query3, 'variables' : vars}

# r = requests.post(url=apiURL, json=data, headers=headers) # make request
# print(r.json())

######### test 4: create new item with graphql variables #########
query4 = 'mutation ($myItemName: String!, $columnVals: JSON!) { create_item (board_id:558120502, item_name:$myItemName, column_values:$columnVals) { id } }'
vars = {
 'myItemName' : 'Assign to Dyna and Senadz!',
 'columnVals' : json.dumps({
   'status' : {'label': 'Done'},
    'person' : {'id' : 257954, 'kind' : 'team'}

 })
}

data = {'query' : query4, 'variables' : vars}
r = requests.post(url=apiURL, json=data, headers=headers) # make request
print(r.json())