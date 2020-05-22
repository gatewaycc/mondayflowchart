import sys
import requests

myToken = 'eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjQ1OTMxNzY3LCJ1aWQiOjEyODQ1MjQ3LCJpYWQiOiIyMDIwLTA1LTIxVDE1OjE0OjEzLjAwMFoiLCJwZXIiOiJtZTp3cml0ZSJ9.pb_aeigPqG3pgiaeaxMaYydfFJtbnBiCtOxXYKDF3Vg'
myUrl = 'http://api.monday.com/v2'
head = {'Authorization' : 'token {}'.format(myToken)}
x = requests.get(myUrl, headers=head)

test1 = open('test1.txt', 'w')

y = int(x.status_code)

print (y + 1, file = test1 )

t = x.json()

print(t, file=test1)

test1.close()