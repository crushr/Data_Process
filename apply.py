# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=4V2lQUe6uPLH078e8vbUXjys&client_secret=eF4R3WE3LK4hc3z3rGuQFHEICmf0iGhF'
response = requests.get(host)
if response:
    print(response.json())