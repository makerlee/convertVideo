from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json
from django_demo.GetVideo import GetVideo


def to_login(request):
    return render(request=request, template_name="login.html", context={"a": "aaa"})


def login(request):
    email = request.POST['email']
    passwd = request.POST['passwd']
    if email == '123@qq.com' and passwd == 'admin':
        request.session['user11'] = email
        return HttpResponseRedirect("index")
    else:
        return render(request, "login.html", context={"reason": "1000"})


# 主页
def index(request):
    user = request.session.get("user11", "--")
    if user == "--":
        return render(request, "login.html", context={"reason": "1001"})
    return render(request, "index.html", context={"user": user})


def signout(request):
    request.session.delete("user11")
    return HttpResponse(json.dumps({"code": 200}), content_type="application/json")


# 调用iiiLab第三方视频解析接口 makermade  jsk111222
# http://static.iiilab.com/iiiLab_video_api_v1.pdf
def convertURL(request):
    fail = {
        "retCode": 1000,
        "retDesc": "你输出的网址不合法"
    }
    original = request.POST['originalURL']
    if original.strip() == "":
        return HttpResponse(json.dumps(fail), content_type="application/json")
    client = GetVideo(link=original)
    data = client.get_data()
    print(data)
    return HttpResponse(json.dumps(data), content_type="application/json")
