import mitmproxy.http
import logging,sys

# https://blog.wolfogre.com/posts/usage-of-mitmproxy/#%E7%A4%BA%E4%BE%8B
# https://blog.csdn.net/tangguoxing000/article/details/102900512

logging.basicConfig(filename=sys.path[0]+'/'+__name__+'.log',format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.INFO,filemode='a',datefmt='%Y-%m-%d%I:%M:%S %p')


# http static resource file extension
static_ext = ['js', 'css', 'ico', 'jpg', 'png', 'gif', 'jpeg', 'bmp', 'conf']
# media resource files type
media_types = ['image', 'video', 'audio']
 
# url filter
url_filter = ['dongfeng-nissan','google-analytics','cachi.cigdata']
 
word_filter = ['v2','collect']
 
static_files = [
    'text/css',
    'image/jpeg',
    'image/gif',
    'image/png',
]
 
 
# 词过滤
def wordFilter(url):
    flag = False
    for word in word_filter:
        if url.__contains__(word):
            flag = True
            break
    return flag
 
 
class HttpFilter:
    def response(self, flow: mitmproxy.http.HTTPFlow):
        print("request=====================",flow.request)
        # 忽略相应的地址
        host = flow.request.host
        print("host====",host)
        print("method====",flow.request.method)
        print("status====",flow.response.status_code)
        print("url====",flow.request.url)
        print("lastPath====",flow.request.url.split('?')[0].split('/')[-1])
        # if host in url_filter:
        #     print("url_filer====",flow.request)
        #     # return
 
        # if not flow.request.method == "GET":
        #     print("get=====",flow.request)
        #     # return
 
        # if not flow.response.status_code == 200:
        #     print("200====",flow.request)
        #     # return
 
        # # 忽略相应的请求
        # url = flow.request.url
        # if wordFilter(url):
        #     print("word_filter====",flow.request)
        #     # return
        # lastPath = url.split('?')[0].split('/')[-1]
        # print("lastPath====",lastPath)
        # if lastPath.split('.')[-1] in static_ext:
            # return
        
        # if flow.response.text.__contains__('<html'):
            # logging.info(flow.request.pretty_url)
 
 
addons = [
    HttpFilter()

]