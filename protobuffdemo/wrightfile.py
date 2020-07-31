# -*- coding: utf-8 -*-

from message_pb2 import Message
import os
from pathlib import Path
import time

base_dir=Path(__file__).resolve().parent



if __name__ == "__main__":

    for i in range(5):
        
        uid = "testjmeter3uid"+str(i).zfill(18)
        sid = "testjmeter3sid"+str(i).zfill(18)
        vid = "testjmeter3vid"+str(i).zfill(18)
        for j in range(5):
            now = int(time.time()*1000)
            ts = now
            data = '[{"id":0,"x":0,"p":%s,"d":{"userId":"%s","name":"iMedia","content":"https://imedia-qa.cigdata.cn/cig/general/#/ConversionFNL?_k=z0xiyo","source":{"protocol":"https","domain":"imedia-qa.cigdata.cn","path":"/cig/general/","hash":"#/conversionfnl?_k=z0xiyo"},"payload":{"interactive":2445,"dcl":2445,"uid":"admin","dimension1":"%s","dimension2":"admin"},"generationTime":5235,"m":false,"url":"https://imedia-qa.cigdata.cn/cig/general/#/ConversionFNL?_k=z0xiyo","t":"iMedia","dtm":%s,"sz":{"w":1366,"h":768},"f":"https://imedia-qa.cigdata.cn/cig/general/","et":18},"t":0}]' %(j,uid,uid,now)
            size = len(data)
            line = uid + "\t" + sid + "\t" + vid + "\t" + str(ts) + "\t" + str(size) + "\t" + data
            print(line)
            time.sleep(0.03)