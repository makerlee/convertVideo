from django.shortcuts import render
from django.http import HttpResponse
import json
import hashlib


def to_login(request):
    return render(request=request, template_name="login.html", context={"a": "aaa"})


def login(request):
    email = request.POST['email']
    passwd = request.POST['passwd']
    if email == '123@qq.com' and passwd == 'admin':
        return render(request, "index.html", context={"user": email})
    else:
        return render(request, "login.html", context={"reason": "1000"})


# 调用iiiLab第三方视频解析接口
# http://static.iiilab.com/iiiLab_video_api_v1.pdf
def convertURL(request):
    orignal = request.POST['originalURL']

    data = {
        "text": "你好呀",
        "cover": "封面",
        "video": "http://www.youtube.com/adee12dad"
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
