# -*- coding: utf-8 -*-

from ProtobufHandle_pb2 import Request, Response
from flask import Flask, request


app = Flask(__name__)


@app.route("/protobuf", methods=["POST"])
def _protobuf():
    # 解析请求
    req = Request()
    req.ParseFromString(request.get_data())
    print(req)
    if req.cate_id == 'xiwang':
        # 编写响应
        res = Response()
        res.code = 200
        d1 = res.data()
        d1.id = "1"
        d1.title = "哈哈"
        d2 = res.data()
        d2.id = "2"
        d2.title = "嘿嘿"
        res.dataList.append(d1)
        res.dataList.append(d2)
        return res.SerializeToString(), 200
    else:
        return "bad",201

if __name__ == '__main__':
    app.run("0.0.0.0", port=8899)