import hashlib
import requests
import json
import time


# 视频解析接口调用类
# clientSecretKey:6c355ed087b2324311a14340fd7d066a
class GetVideo:

    def __init__(self, link):
        self.link = link
        self.url = "http://service.iiilab.com/video/download"
        self.clientid = "b5d44b31a01de013"

    def get_data(self):
        # md5(link + timestamp + secretKey)
        timestamp = str(time.time()*1000).split(".")[0]
        data = self.link + timestamp + "6c355ed087b2324311a14340fd7d066a"
        data = data.encode()
        sign = hashlib.md5(data).hexdigest()
        data = {
            "link": self.link,
            "timestamp": timestamp,
            "sign": sign,
            "client": self.clientid
        }
        result = requests.post(self.url, params=data)
        data = result.json()
        return data




