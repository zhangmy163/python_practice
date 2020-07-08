# ex1 

requests.get


# ex2

requests.post

如果返回的是json可以使用response.json()来获取响应

# ex3

代理

可以使用环境变量，这样在request请求时可以不用带proxies参数

```
import os
os.environ['HTTP_PROXY'] = proxies['http']
os.environ['HTTPS_PROXY'] = proxies['https']
```

