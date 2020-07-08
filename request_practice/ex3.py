# -*- coding:utf-8 -*-
import os
import requests

proxies={
    "http":"http://127.0.0.1:1080",
    "https":"https://127.0.0.1:1080"
}

# os.environ['HTTP_PROXY'] = proxies['http']
# os.environ['HTTPS_PROXY'] = proxies['https']
response1 = requests.get("https://www.baidu.com",proxies=proxies)
print(response1.status_code)

response2 = requests.get("https://www.google.com",proxies=proxies)
print(response2.status_code)