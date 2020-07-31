# -*- coding: utf-8 -*-

from ProtobufHandle_pb2 import Request, Response
import requests


def test_protobuf():
    """
    test
    :return:
    """
    req = Request()
    req.cate_id = "xiwang1"
    req.page = 1
    req.pageSize = 10
    req_data = req.SerializeToString()
    print(req_data)
    response = requests.post("http://127.0.0.1:8899/protobuf", data=req_data)
    print("reponse==========",response)
    # print("res.json",response[2].json())
    res = Response()
    
    res.ParseFromString(response.content)
    print("res=============",res)
    for i in res.dataList:
        print("title=======",i.title)


if __name__ == '__main__':
    test_protobuf()