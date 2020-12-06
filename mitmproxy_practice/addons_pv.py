import mitmproxy.http
import logging
from pathlib import Path
base_dir=Path(__file__).resolve().parent
logfile=str(base_dir)+"/log.txt"
# https://blog.wolfogre.com/posts/usage-of-mitmproxy/#%E7%A4%BA%E4%BE%8B
# https://blog.csdn.net/tangguoxing000/article/details/102900512

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler(logfile)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class HttpFilter:
    def response(self, flow: mitmproxy.http.HTTPFlow):
        # print("request=====================",flow.request)
        
        # host = flow.request.host
        url = flow.request.url
        scode = flow.response.status_code
        text = flow.request.get_text()

        # print("pretty====",flow.request.pretty_url)
        # print("method====",flow.request.method)
        # print("lastPath====",flow.request.url.split('?')[0].split('/')[-1])

        if( 'google-analytics' in url and "collect" in url and scode == 200 ):
            if('pageview' in url):
                logger.info("GA pageview code====: "+url)
        if( 'cachi.cigdata' in url and 'event' in url and scode == 202 ):
            # logger.info("text ==========:"+text)
            if(':18}' in text):
                logger.info("CIGA pageview code====: "+url)
 
addons = [
    HttpFilter(),
]