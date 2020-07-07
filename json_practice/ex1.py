# -*- coding:utf-8 -*-

import json
 
# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)

# Python 字典类型转换为 JSON 对象
data1 = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : True,
    'none' : None
}
 
json_str = json.dumps(data1,)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])


data3={
    'code': 0,
    'message': "返回正常",
    'data':{
        'result':[
            {
                'name':'zhangsan',
                'age':18
            },
            {
                'name':'lisi',
                'age':15
            }
        ]
    }
}
json_str = json.dumps(data3)
data4 = json.loads(json_str)
print("=========================")
print("data3['codoe']: ",data4['code'])
print("data3['message']: ",data4['message'])
print("data3['data']: ",data4['data'])
print("data3['result']: ",data4['data']['result'])
print("data3['result1']: ",data4['data']['result'][0])
print("data3['result1_name']: ",data4['data']['result'][0]['name'])
print("data3['result1_age']: ",data4['data']['result'][0]['age'])
print("=========================")


# 写入 JSON 数据
with open('./json_practice/data.json', 'w') as f:
    json.dump(data4, f)
 
# 读取数据
with open('./json_practice/data.json', 'r') as f:
    data = json.load(f)
print(data)