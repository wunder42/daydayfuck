# -*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from official import WxRequest, WxTextResponse
import hashlib
# from bae.api import logging
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt 
from utils import Weather, BaiduBus
from django.views.generic import TemplateView
import json

@csrf_exempt
def index(request): 
    signature = request.GET.get("signature", None)  
    timestamp = request.GET.get("timestamp", None)  
    nonce = request.GET.get("nonce", None)  
    echoStr = request.GET.get("echostr",None) 
    token = "dianyiwx"
    if request.method == 'GET':  
        tmpList = [token,timestamp,nonce]  
        tmpList.sort()
        tmpstr = "%s%s%s" % tuple(tmpList) 
        tmpstr = hashlib.sha1(tmpstr).hexdigest()  
        if tmpstr == signature:  
            return HttpResponse(echoStr)
    req = WxRequest(request.body)
    # logging.info(req)
    if req.MsgType == 'text':
        # return HttpResponse(WxTextResponse(req.Content, req).as_xml())
        return parseText(req.Content, req)
    elif req.MsgType == 'event' and req.Event == 'subscribe':
        return HttpResponse(WxTextResponse(u'欢迎来到小刀的世界，因为我你不再寂寞。。。请按提示操作：0.帮助文档 1.冷笑话',
                                           req).as_xml())
    else:
        return HttpResponse(WxTextResponse('嘿，小心使用！',
                                           req).as_xml())
    return HttpResponse("error")

def parseText(text, req):
    if '1' == text:
        '''冷笑话'''
        content = u"芝忠说：好巧哦，在广州遇见你。小毛说：是是是，心灵手巧而已 —— ——！！！"
    elif '0' == text:
        '''帮助文档'''
        content = u"0.帮助文档 1.冷笑话 2.广州天气 3."
    elif '2' == text:
        '''广州天气'''
        weather = Weather()
        req_text = "%s|%s|%s|%s" % (weather.temp[0], weather.weather[0], weather.wind[0], weather.index)
        return HttpResponse(WxTextResponse(req_text, req).as_xml())
    else:
        content = u"别整那些没用的！！！"
    return HttpResponse(WxTextResponse(content, req).as_xml())

class RegisterView(TemplateView):
    template_name = 'wx-dy-base.html'

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        return context

@csrf_exempt
def add_register(request):
    # return HttpResponse("ABC")
    succ = False
    if 'POST' == request.method:
        try:
            name = request.POST.get('name', None)
            college = request.POST.get('college', None)
            qq = request.POST.get('qq', None)
            course = request.POST.get('select', None)

            if name and college and len(qq)>8 and course:
                succ = True
            res = json.dumps({'name':name, 'college':college, 'succ':succ, 'qq':qq, 'course':course})
            # return HttpResponse(res, mimetype="application/json")
            # return HttpResponseRedirect('/success/')
            return render_to_response('result.html', {'result': succ})
        except:
            pass
    # return HttpResponse(json.dumps({}), mimetype="application/json")
    return render_to_response('result.html', {'result': succ})
