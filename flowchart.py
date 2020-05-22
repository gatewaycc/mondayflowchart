import json
import urllib.request
from monday import MondayClient


monday = MondayClient('eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjQ1NzQ0NzA1LCJ1aWQiOjEyODI1OTM2LCJpYWQiOiIyMDIwLTA1LTE5VDE5OjA0OjI1LjAwMFoiLCJwZXIiOiJtZTp3cml0ZSJ9.C76pJ4PMUnnFy_vM09MwwnENohxhRMhA56TmLJ7p-lE')

monday.items.create_item(board='558120502', group='topics', item='We be automating!')
