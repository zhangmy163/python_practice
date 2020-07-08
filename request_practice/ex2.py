# -*- coding:utf-8 -*-
import requests,json

url="https://xx.xx.xx/submit/user/information"
p_data={
    "city": "python",
    "name": "test",
    "phone": 13812345678
}
post_data=json.dumps(p_data)
headers={"Content-Type":"application/json"}

respose = requests.post(url,data=post_data,headers=headers)

# print(respose.url)
print(respose.json())