
# encoding:utf-8

import requests
import base64

'''
通用物体和场景识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
# 二进制方式打开图片文件
f = open('/Users/zhongshannan/Documents/fakenews_detection/dataset/weiboA/images/3d276f0fgw1edhme4vl05j20b40fsglv.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.05e99890b323593a52dcc48ba0e33b9c.2592000.1652362639.282335-25954805'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())