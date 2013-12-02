#! -*- coding:utf-8 -*-
import os, hashlib, json, re
import pymongo
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.conf import settings

from official import WxRequest, WxTextResponse
from utils import Weather, BaiduBus
from models import Wxuser


if 'SERVER_SOFTWARE' in os.environ:
    from bae.api import logging
    from bae.api.memcache import BaeMemcache
    from bae.core import const

    con = pymongo.Connection(host = const.MONGO_HOST, port = int(const.MONGO_PORT))
    db = con[settings.DB_NAME]
    db.authenticate(const.MONGO_USER, const.MONGO_PASS)
    cache = BaeMemcache()
else:
    import logging
    from django.core.cache import cache
    con = pymongo.Connection(host = settings.MONGO_HOST, port = int(settings.MONGO_PORT))
    db = con[settings.DB_NAME]
    # db.authenticate(settings.MONGO_USER, settings.MONGO_PASS)

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
    logging.info('parse2deal')
    if not cache.get(request.FromUserName, None):
        _item = db.t_user.find_one({'openid':request.FromUserName})
        logging.info(_item)
        if not _item:
            user = Wxuser.create_user(request.FromUserName)
            cache_value = '''{"openid":"%s", "jokeTimestamp":"%s"}''' % (request.FromUserName, -1)
            cache.set(request.FromUserName, cache_value)
        else:
            cache_value = '''{"openid":"%s", "jokeTimestamp":"%s"}''' % (request.FromUserName, _item['jokeTimestamp'])
            cache.set(request.FromUserName, cache_value)
    logging.info(cache.get(request.FromUserName))
    if 'event' == request.MsgType and 'subscribe' == request.Event:
		return HttpResponse(WxTextResponse(u'welcome daydayHappy family...', request).as_xml())
    elif 'text' == request.MsgType:
        _t = re.findall('xh|joke|笑话|xiaohua|haha|哈哈', request.Content)
        if len(_t) > 0:
            _tmp = json.loads(cache.get(request.FromUserName))
            logging.info(_tmp)
            _joke = int(_tmp.get('jokeTimestamp', -1))
            if 1:
                _item = [i for i in db.text_joke.find({'jokeTimestamp':{'$gt':_joke}}).sort('jokeTimestamp').limit(1)]
                if not len(_item): return HttpResponse(WxTextResponse(u'no new jokes...', request).as_xml())
                logging.info(len(_item))
                _item = _item[0]
                _content, _timestamp = _item['content'], int(_item['jokeTimestamp'])

                Wxuser.update_user(_tmp['openid'], **{'jokeTimestamp':_timestamp})
                cache_value = '''{"openid":"%s", "jokeTimestamp":"%s"}''' % (_tmp['openid'], _timestamp)
                cache.set(_tmp['openid'], cache_value)

                return HttpResponse(WxTextResponse(unicode(_content), request).as_xml())
	return HttpResponse(WxTextResponse('error parse', request).as_xml())

'''
request deal
'''

def clear_cache(request):
    cache.clear()
    return HttpResponse(json.dumps({'successful':True}), 'application/json')

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

