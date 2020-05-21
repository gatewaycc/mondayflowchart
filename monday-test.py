##Import Support Files and Monday API
import json
import urllib.request
from monday import MondayClient

##Connect to Monday.com using Token
MondayClient('eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjQ1OTMxNzY3LCJ1aWQiOjEyODQ1MjQ3LCJpYWQiOiIyMDIwLTA1LTIxVDE1OjE0OjEzLjAwMFoiLCJwZXIiOiJtZTp3cml0ZSJ9.pb_aeigPqG3pgiaeaxMaYydfFJtbnBiCtOxXYKDF3Vg')

##Test Create new Item - Successful
monday.items.create_item(board='558120502', group='topics', item='Do another thing now!')
