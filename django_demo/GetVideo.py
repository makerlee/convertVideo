import hashlib

import requests
import json


# 视频解析接口调用类
class GetVideo:

    def __init__(self):
        self.url = "http://service.iiilab.com/video/download"
        self.link = ""
        self.timestamp = ""
        self.clientid = "123"

    def get_data(self):
        # md5(link + timestamp + secretKey
        sign = hashlib.md5(self.link)
        sign = sign.hexdigest()
        data = {
            "link": self.link,
            "timestamp": self.timestamp,
            "sign": sign,
            "client": self.clientid
        }
        result = requests.post(self.url, params=data)
        data = result.json()
        return json.dumps(data)


