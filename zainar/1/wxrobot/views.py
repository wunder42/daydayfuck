#! -*- coding:utf-8 -*-
import hashlib, json, logging
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from official import WxRequest, WxTextResponse
from utils import Weather, BaiduBus

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
    return parse2deal(req)

def parse2deal(request):
	logging.info(request)

	if 'event' == request.MsgType and 'subscribe' == request.Event:
		return HttpResponse(WxTextResponse(u'welcome daydayHappy family...', request).as_xml())
	elif 'text' == request.MsgType:
		return HttpResponse(WxTextResponse(u'...', request).as_xml())
	else:
		return HttpResponse(WxTextResponse('error parse', request).as_xml())



'''
other service
'''
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

