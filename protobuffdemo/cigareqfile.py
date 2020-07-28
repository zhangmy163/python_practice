# -*- coding: utf-8 -*-

from message_pb2 import Message
import os
from pathlib import Path
base_dir=Path(__file__).resolve().parent

if __name__ == "__main__":
    req = Message()
    reqMc = req.context.add()
    reqMp = req.packet.add()
    
    req.cid = "xxx"
    req.uid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    req.sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    req.domain = "xxx.xxx.xxx.xxx"
    
    reqMc.ln = "xxx"
    reqMc.lv = "xxx"
    # reqMc.ip = "xxx"
    reqMc.ref = "xxxxxxxxxxxxxx"
    # reqMc.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    reqMp.vid = "xxxxx"
    reqMp.ts = 1595899817122
    reqMp.status = 0
    reqMp.size = 123
    reqMp.data = bytes('xxxxxxxx', encoding='utf-8')
    # reqMp.payload[''] = b''

    # print(req)
    req_data = req.SerializeToString()

    with open(file=str(base_dir)+"/file/cigareq.f",mode="wb") as f:
        f.write(req_data)

    
    # from google.protobuf.message import DecodeError
    # res = Message()
    # rf= open(str(base_dir)+"/file/cigareq.f", "rb")
    # for r in rf:
    #     print("========r=======",r)
    #     try:
    #         print("sssss",res.ParseFromString(r))
    #     except DecodeError :
    #         continue
        
    # rf.close()
    # print(res.ParseFromString(b'\x03Web\x12\x051.0.3")https://imedia-qa.cigdata.cn/cig/general/\n'))

