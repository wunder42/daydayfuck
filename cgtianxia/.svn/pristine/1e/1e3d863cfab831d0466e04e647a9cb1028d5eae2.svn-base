# -*- coding=utf-8 -*-
import os
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import DyNews, DyAdInfo, DyJobInfo, DyStuOpusInfo, DyCourseNews, DyClass, Tiny, DyCourse, DyCourseClass, Liuyan
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from forms import SignupForm, LiuyanForm
from context_processors import course_list_proc
import json

course_list = DyCourse.objects.order_by("id")
course_choice, k = [], 1
for course in course_list:
    course.course_class = course.dycourseclass_set.all()

def get_course_list():
    course_list = DyCourse.objects.order_by("id")
    for course in course_list:
        course.course_class = course.dycourseclass_set.all()
    return course_list

def focus(request, page_id):
    dy_focus = DyAdInfo.objects.get(id=int(page_id))
    dy_focus_pre, dy_focus_next = 0, 0
    try:
        dy_focus_pre = DyAdInfo.objects.get(id=int(page_id)+1)
    except:
        pass
    try:
        dy_focus_next = DyAdInfo.objects.get(id=int(page_id)-1)
    except:
        pass
    hot_dy_focus_list = DyAdInfo.objects.order_by('-id')[:5]

    return render_to_response('focus.htm', {'dy_focus':dy_focus, 'dy_focus_pre':dy_focus_pre, 'dy_focus_next':dy_focus_next, 'course_list':course_list, 'hot_dy_focus_list':hot_dy_focus_list})

def index(request, template_name):
    ad_pic_list = DyAdInfo.objects.order_by('-id')[:4]
    opus_list = []
    dy_news_list = DyNews.objects.all()[:6]
    course_news_list = DyCourseNews.objects.all()[:6]
    class_list = DyClass.objects.order_by("-id")[:6]
    course_list = DyCourse.objects.order_by("id")
    course_class_list = DyCourseClass.objects.all()
    for course in course_list:
        course.course_class = course.dycourseclass_set.all()
    if 'SERVER_SOFTWARE' in os.environ:
        import sae.storage
        s = sae.storage.Client()
        for index in range(len(ad_pic_list)):
            ad_pic_list[index].image = s.url('upload', 'navs/' + str(ad_pic_list[index].image))
        for course in course_list:
            t = DyStuOpusInfo.objects.filter(course_category__in=course.course_class).order_by('-id')[:5]
            for x in t:
                x.image = s.url('upload', 'opus/' + str(x.image))
            opus_list.append(t)
    else:
        ad_pic_list = list()
        for x in range(5):
            ad_pic_list.append({'id':x+1, 'author':'mao xiao bao' + str(x), 'title':'i am chen', 'content':'nothing is poss', 'image':'/static/images/slider_a.jpg'})
        opus_list.append(ad_pic_list)
    job_list = DyJobInfo.objects.order_by('-id')[:4]
    for job in job_list:
        job.course_class = job.name.course_class.all()[0]
    return render_to_response(template_name, locals())

def news(request, page, template_name, model, url_type=None, course_type=None):
    if course_type and int(course_type)==0 or course_type==None:
        dy_list = model.objects.order_by("-id")
    elif course_type:
        if url_type == "course":
            dy_list = model.objects.filter(course_category=int(course_type)).order_by("-id")
        elif url_type =="opus":
            dy_list = model.objects.filter(course_category__in=course_list[int(course_type)-1].course_class).order_by("-id")
    if course_type and 'SERVER_SOFTWARE' in os.environ:
        import sae.storage
        s = sae.storage.Client()
        for dy in dy_list:
            dy.image = s.url('upload', url_type + '/' + str(dy.image))
    else:
        if url_type == 'opus':
            dy_list = []
            for x in range(24):
                dy_list.append({'id': x+1, 'title': str(x)+"man", 'author': str(x) + 'xiao bao', 'image': '/static/images/slider_a.jpg'})

    paginator = Paginator(dy_list, 6)
    after_range_num, before_range_num, page_range = 6, 5, 0
    page = int(page)
    try:
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    try:
        coms = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        coms = paginator.page(1)
    if page >= after_range_num:
        page_range = paginator.page_range[page - after_range_num: page + before_range_num]
    else:
        page_range = paginator.page_range[0: page + before_range_num]
    return render_to_response(template_name, {'hot_list':dy_list[:6], 'coms':coms, 'page_range':page_range, 'course_type':course_type}, context_instance=RequestContext(request, processors=[course_list_proc, ]))

def news_display(request, nid, template_name, model, url_type=None):
    dy_pre, dy_next = 0, 0
    try:
        dy_pre = model.objects.get(id=int(nid)+1)
    except:
        pass
    try:
        dy_next = model.objects.get(id=int(nid)-1)
    except:
        pass
    dy = model.objects.get(id=int(nid))
    hot_list = model.objects.order_by("-id")[:5]
    if url_type=='course':
        form = LiuyanForm()
        cid = model.objects.get(id=int(nid))
        liuyan_list = Liuyan.objects.filter(course_id=cid)
        author, mail = '', ''
        if 'author' in request.COOKIES and 'mail' in request.COOKIES:
            author, mail = request.COOKIES['author'], request.COOKIES['mail']
        return render_to_response(template_name, {'dy':dy, 'dy_pre':dy_pre, 'dy_next':dy_next, 'hot_list':hot_list, 'form':form, 'liuyan_list':liuyan_list, 'author':author, 'mail':mail}, context_instance=RequestContext(request, processors=[course_list_proc, ]))
    return render_to_response(template_name, {'dy':dy, 'dy_pre':dy_pre, 'dy_next':dy_next, 'hot_list':hot_list}, context_instance=RequestContext(request, processors=[course_list_proc, ]))

def opus_display(request, cid, oid, template_name, model):
    opus_list = []
    if 'SERVER_SOFTWARE' in os.environ:
        import sae.storage
        s = sae.storage.Client()
        if not cid:
            opus_list = model.objects.all()
        else:
            opus_list = model.objects.filter(course_category__in=get_course_list()[int(cid)-1].course_class)
        for op in opus_list:
            op.image = s.url('upload', 'opus/' + str(op.image))
    else:
        for x in range(5):
            opus_list.append({'id':x+1, 'author':'mao xiao bao' + str(x), 'title':'i am chen', 'content':'nothing is poss', 'image':'/static/images/slider_a.jpg'})
    # try:
    #     opus_list = None
    #     if not cid:
    #         opus_list = model.objects.all()
    #     else:
    #         opus_list = model.objects.filter(course_category__in=get_course_list()[cid-1].course_class)
    # except:
    #     pass
    return render_to_response(template_name, {'opus_list':opus_list, 'oid':oid}, context_instance=RequestContext(request, processors=[course_list_proc,]))

def setting(request, cid, model, template_name):
    dy = model.objects.get(id=int(cid))
    form = SignupForm()
    return render_to_response(template_name, {"dy":dy, 'form':form}, context_instance=RequestContext(request, processors=[course_list_proc, ]))

def class_info(request, page_id):
    classinfo = DyClass.objects.get(id=int(page_id))
    hot_class_list = DyClass.objects.order_by("-id")
    
    return render_to_response('class_info.htm', {'classinfo':classinfo, 'course_list':course_list,'hot_class_list':hot_class_list,'paths':paths})

# def opus_display(request, oid):
#     opus_list = []
#     for x in range(12):
#         opus_list.append({'id':x+1, 'author':'mao xiao bao', 'title':'i am chen', 'content':'nothing is poss', 'image':'/static/images/slider_b.jpg'})
#     return render_to_response('opus.htm', {'course_list':course_list, 'opus_list':opus_list})

def check_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            from django.core.mail import send_mail
            send_mail('点艺--报名--信息--来自33she','---'.join([cd.get('name', '姓名'), cd.get('college', '学校'), cd.get('phone', '电话'), cd.get('qq', 'QQ'), cd.get('mail', '邮箱'), cd.get('course', '课程')]), 'maozeizei@qq.com',['maohuguang09@nou.com.cn'],)
            return HttpResponseRedirect('/dyhome/thanks/')
    else:
        form = SignupForm()
    return render_to_response('course_setting.htm',{'form': form, 'course_list':course_list},context_instance=RequestContext(request))

def liuyan(request, lid, model, GET=None, POST=None):
    if request.method == 'GET' and GET is not None:
        return GET(request, lid, model)
    elif request.method == 'POST' and POST is not None:
        return POST(request, lid, model)
    raise Http404

def liuyan_get(request, lid, model):
    pass

def liuyan_post(request, lid, model):
    assert request.method == "POST"
    form = LiuyanForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        ci = model.objects.get(id=int(lid))
        li = None
        import time
        aliuyan = Liuyan.objects.create(course_id=ci, liuyan_id=li, author=cd.get('name', '匿名'), mail=cd.get('mail', '邮箱'), content=cd.get('content', '内容'), publication_date="2013-04-09 12:13")
        response = HttpResponseRedirect('/dyhome/course_display/' + lid)
        author, mail = cd.get('name', '姓名').encode('utf-8'), cd.get('mail', '邮件').encode('utf-8')
        response.set_cookie('author', author)
        response.set_cookie('mail', mail)
        return response
        # return HttpResponseRedirect('/dyhome/course_display/' + lid)
    # else:
    #     form = LiuyanForm()
    # return render_to_response('course_display.htm', {'form': form, 'course_list':course_list}, context_instance=RequestContext(request))

def test_liuyan_post(request, lid, last_liuyan_id,  model):
    if True:
        # cd = form.cleaned_data
        ci = model.objects.get(id=int(lid))
        li = None
        import time
        # aliuyan = Liuyan.objects.create(course_id=ci, liuyan_id=li, author=cd.get('name', '匿名'), mail=cd.get('mail', '邮箱'), content=cd.get('content', '内容'), publication_date="2013-04-09 12:13")
        # response = HttpResponseRedirect('/dyhome/course_display/' + lid)
        liuyan_cookie = {}
        # author, mail = cd.get('name', '姓名').encode('utf-8'), cd.get('mail', '邮件').encode('utf-8')
        # liuyan_cookie['author'], liuyan_cookie['mail'] = author, mail
        liuyan_set_query = Liuyan.objects.filter(course_id=ci).filter(id__gt=str(last_liuyan_id))
        liuyan_list = []
        for liuyan in liuyan_set_query:
            liuyan_list.append({'id':liuyan.id,'author':liuyan.author, 'mail':liuyan.mail, 'content':liuyan.content})
        liuyan_dict = {'data':liuyan_list, 'cookie':liuyan_cookie}
        return HttpResponse(json.dumps(liuyan_dict, ensure_ascii=False), mimetype="application/json")
    else:
        pass
def thanks(request):
    return render_to_response('thanks.htm', locals())

def base_display(request, template_name):
    return render_to_response(template_name, context_instance=RequestContext(request))

if __name__ == "__main__":
    pass

# def opus(request, op, page):
#     if 0 == int(op):
#         opus_list = DyStuOpusInfo.objects.order_by('-id')
#     else:
#         try:
#             opus_list = DyStuOpusInfo.objects.filter(course_category__in=course_list[int(op)-1].course_class).order_by("-id")
#         except:
#             opus_list = DyStuOpusInfo.objects.order_by('-id')
#             op, page = 0, 1
#     if 'SERVER_SOFTWARE' in os.environ:
#         import sae.storage
#         s = sae.storage.Client()
#         for opus in opus_list:
#             opus.image = s.url('upload', 'opus/' + str(opus.image))
#     else:
#         opus_list = []
#         for x in range(24):
#             opus_list.append({'id': x+1, 'title': str(x)+"man", 'author': str(x) + 'xiao bao', 'image': '/static/images/slider_a.jpg'})
#     page = int(page)
#     paginator = Paginator(opus_list, 6)
#     after_range_num, before_range_num = 6, 5
#     try:
#         if page<1:
#             page = 1
#     except ValueError:
#         page = 1
#     try:
#         coms = paginator.page(page)
#     except (EmptyPage, InvalidPage, PageNotAnInteger):
#         coms = paginator.page(1)
#     if page >= after_range_num:
#         page_range = paginator.page_range[page - after_range_num: page + before_range_num]
#     else:
#         page_range = paginator.page_range[0: page + before_range_num]
#     
#     return render_to_response("opus_list.htm", {"course_list":course_list, 'coms':coms, 'page_range':page_range, 'paths':paths, 'op':op})


# def course(request, course, page):
#     if 0 == int(course):
#         course_news_list = DyCourseNews.objects.order_by("-id")
#     else:
#         course_news_list = DyCourseNews.objects.filter(course_category=int(course)).order_by("-id")
#     if 'SERVER_SOFTWARE' in os.environ:
#         import sae.storage
#         s = sae.storage.Client()
#         for news in course_news_list:
#             news.image = s.url('upload', 'courses/' + str(news.image))
#     page = int(page)
#     paginator = Paginator(course_news_list, 6)
#     after_range_num, before_range_num = 6, 5
#     try:
#         if page<1:
#             page = 1
#     except ValueError:
#         page = 1
#     try:
#         coms = paginator.page(page)
#     except (EmptyPage, InvalidPage, PageNotAnInteger):
#         coms = paginator.page(1)
#     if page >= after_range_num:
#         page_range = paginator.page_range[page - after_range_num: page + before_range_num]
#     else:
#         page_range = paginator.page_range[0: page + before_range_num]
#     paths = [{'url':'/dyhome', 'name':"index"}, {'url':'/dyhome/', 'name':"about dianyi"}]
    
#     hot_course_news_list = DyCourseNews.objects.order_by("-id")
#     return render_to_response("course.htm", {'course_news_list':course_news_list, 'course_list':course_list, 'hot_course_news_list':hot_course_news_list,'paths':paths, 'coms':coms, 'page_range':page_range,'course':course})

# def myhome_(request):

#     ad_pic_list = [{'id':1, 'author':'mao xiao bao', 'title':'i am chen', 'content':'nothing is poss', 'image':'/static/images/slider_a.jpg'}, {'id':2, 'author':'mao xiao bao', 'title':'i am chen', 'content':'nothing is poss', 'image':'/static/images/slider_b.jpg'}, {'id':3, 'author':'mao xiao bao', 'title':'i am chen', 'content':'nothing is poss', 'image':'/static/images/slider_c.jpg'}, {'id':4, 'author':'mao xiao bao', 'title':'i am chen', 'content':'nothing is poss', 'image':'/static/images/slider_a.jpg'}, {'id':5, 'author':'mao xiao bao', 'title':'i am chen', 'content':'nothing is poss', 'image':'/static/images/slider_a.jpg'}]
#     opus_list = []
#     dy_news_list = DyNews.objects.order_by("-id")[:6]
#     course_news_list = DyCourseNews.objects.order_by("-id")[:6]
#     class_list = DyClass.objects.order_by("-id")[:6]
#     course_list = DyCourse.objects.order_by("id")
#     course_class_list = DyCourseClass.objects.all()
#     ccl = []
#     for course in course_list:
#         course.course_class = course.dycourseclass_set.all()
#         t = []
#         for course_class in course_class_list:
#             if course_class.name.name == course.name:
#                 t.append(course.name)
#         ccl.append(t)
#     job_list = DyJobInfo.objects.order_by('-id')[:5]
#     for job in job_list:
#         job.course_class = job.name.course_class.all()[0]
    
#     return render_to_response('myhome.htm', locals())

# def course_display(request, page_id):
#     course_news = DyCourseNews.objects.get(id=int(page_id))
#     hot_course_news_list = DyCourseNews.objects.order_by("-id")
#     course_news_pre, course_news_next = 0, 0
#     try:
#         course_news_pre = DyCourseNews.objects.get(id=int(page_id)+1)
#     except:
#         pass
#     try:
#         course_news_next = DyCourseNews.objects.get(id=int(page_id)-1)
#     except:
#         pass
#     form = LiuyanForm()
#     cid = DyCourseNews.objects.get(id=int(page_id))
#     liuyan_list = Liuyan.objects.filter(course_id=cid)
#     return render_to_response("course_display.htm", {'course_news':course_news, 'course_news_pre':course_news_pre, 'course_news_next':course_news_next, 'course_list':course_list, 'hot_course_news_list':hot_course_news_list,'paths':paths, 'form':form, 'liuyan_list':liuyan_list}, context_instance=RequestContext(request))

# @csrf_exempt  
# def save(request):  
#     content = request.FILES['file1']  
      
#     from os import environ  
#     online = environ.get("APP_NAME", "")   
  
#     if online:  
#         import sae.const  
#         access_key = sae.const.ACCESS_KEY  
#         secret_key = sae.const.SECRET_KEY  
#         appname = sae.const.APP_NAME  
#         domain_name = "upload"         
          
#         import sae.storage    
#         s = sae.storage.Client()  
#         ob = sae.storage.Object(content.read())  
#         url = s.put(domain_name, "ads/"+content.name, ob)  
#         return render_to_response('upload.htm', {"value":url})  
#     else:  
#         return render_to_response('upload.htm', {"value":"save failed"})  

# def upload(request):
#   return render_to_response('upload.htm')

# def info_display(request, template_name):
#     return render_to_response(template_name, context_instance=RequestContext(request, processors=[course_list_proc, ]))