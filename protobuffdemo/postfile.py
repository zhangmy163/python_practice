# -*- coding: utf-8 -*-

from ProtobufHandle_pb2 import Request, Response
import os
from pathlib import Path
base_dir=Path(__file__).resolve().parent

if __name__ == "__main__":
    req = Request()
    
    req.cate_id = "xiwang"
    req.page = 1
    req.pageSize = 10
    req_data = req.SerializeToString()
    # with open('req.f', 'wb') as f:
    #     f.write(req.SerializeToString())
    with open(file=str(base_dir)+"/file/postfile.f",mode="wb") as f:
        f.write(req_data)

