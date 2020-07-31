# -*- coding: utf-8 -*-

from message_pb2 import Message
import os
from pathlib import Path
import time

base_dir=Path(__file__).resolve().parent



if __name__ == "__main__":

    
    now = int(time.time()*1000)
    # print(now)
    req = Message()
    # reqMc = req.context.add()
    reqMp = req.packet.add()
    
    req.cid = "200-spark"
    req.uid = "testjmeteruidua00000000000000006"
    req.sid = "testjmetersidua00000000000000006"
    req.domain = "imedia-qa.cigdata.cn"
    req.context.ln="Web"
    req.context.lv = "1.0.3"
    # req.context.ip = "121.69.1.10"
    req.context.ref = "https://imedia-qa.cigdata.cn/login/?next=%2Fcig%2Fgeneral%2F"
    # req.context.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    # req.context.ua = "Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045227 Mobile Safari/537.36 MMWEBID/7749 MicroMessenger/7.0.12.1620(0x27000C35) Process/tools NetType/WIFI Language/zh_CN ABI/arm64 "
    # reqMc.ln = "Web"
    # reqMc.lv = "1.0.3"
    # reqMc.ip = "121.69.1.10"
    # reqMc.ref = "https://imedia-qa.cigdata.cn/cig/general/"
    # reqMc.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    reqMp.vid = "testjmetervidua00000000000000001"
    reqMp.ts = now
    reqMp.status = 0
    reqMp.data = bytes('[{"id":0,"x":0,"p":0,"d":{"userId":"29d0320f72b3aff4672817a87b037e89","name":"iMedia","content":"https://imedia-qa.cigdata.cn/cig/general/#/ConversionFNL?_k=z0xiyo","source":{"protocol":"https","domain":"imedia-qa.cigdata.cn","path":"/cig/general/","hash":"#/conversionfnl?_k=z0xiyo"},"payload":{"interactive":2445,"dcl":2445,"uid":"admin","dimension1":"29d0320f72b3aff4672817a87b037e89","dimension2":"admin"},"generationTime":5235,"m":false,"url":"https://imedia-qa.cigdata.cn/cig/general/#/ConversionFNL?_k=z0xiyo","t":"iMedia","dtm":1595899817122,"sz":{"w":1366,"h":768},"f":"https://imedia-qa.cigdata.cn/login/?next=%2Fcig%2Fgeneral%2F","et":18},"t":0}]', encoding='utf-8')
    reqMp.size = len(reqMp.data)
    # reqMp.payload[''] = b''
    print("===========len==",len(reqMp.data))
    print("======req=========\n",req)
    # print("======reqmp=======\n",req.MessagePacket.vid)
    req_data = req.SerializeToString()

    with open(file=str(base_dir)+"/file/cigareq.f",mode="wb") as f:
        f.write(req_data)

    

