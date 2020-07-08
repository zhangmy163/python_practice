# -*- coding:utf-8 -*-
import requests,json

# kw = {'wd':'长城'}
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
# response = requests.get("http://www.baidu.com/s?", params = kw, headers = headers)

# 查看响应内容，response.text 返回的是Unicode格式的数据
# print (response.text)
 
# 查看响应内容，response.content返回的字节流数据
# print (response.content)
 
# 查看完整url地址
# print (response.url)
 
# 查看响应头部字符编码
# print (response.encoding)
 
# 查看响应码
# print (response.status_code)

response = requests.get("https://xx.xx.xx/brand/query/mainBrandList")
d_json = json.loads(response.text)
print(len(d_json['data']))
# print(json_str)

response2 = requests.get("https://xx.xx.xx/brand/query/brandList?",params={"mainBrandId":49},headers=None)

print(response2.url)
d_json2 = json.loads(response.text)
print(d_json2['retcode'])

d_json3 = response2.json()
print(d_json3['retcode'])
