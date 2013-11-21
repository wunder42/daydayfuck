from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.decorators.cache import cache_page
import models, views
# import django.views.generic.simple

urlpatterns = patterns('dyhome.views',
	# url(r'^$', cache_page(views.index, 60*5), {'template_name':'index.htm'}),
	url(r'^$', 'index', {'template_name':'index.htm'}),
	url(r'^news/(?P<page>\d{1,4})/$', 'news', {'template_name':'dynews_list.htm','model':models.DyNews}),
	url(r'^course/(?P<course_type>\d{0,2})/(?P<page>\d{0,2})/$', 'news', {'template_name':'course.htm', 'model':models.DyCourseNews, 'url_type':'course'}),
	url(r'^opus/(?P<course_type>\d{1,2})/(?P<page>\d{1,4})/$', 'news', {'template_name':'opus_list.htm', 'model':models.DyStuOpusInfo, 'url_type':'opus'}),
	url(r'^news_display/(?P<nid>\d+)/$', 'news_display', {'template_name':'dynews.htm', 'model':models.DyNews}),
	url(r'^course_display/(?P<nid>\d+)/$', 'news_display', {'template_name':'course_display.htm', 'model':models.DyCourseNews, 'url_type':'course'}),
	url(r'^courses/(?P<cid>\d{0,2})/$', 'setting', {'template_name':'course_setting.htm', 'model':models.DyCourseClass}),
	url(r'^opus_display/(?P<cid>\d{0,2})/(?P<oid>\d{0,2})/$', 'opus_display', {'template_name':'opus.htm', 'model':models.DyStuOpusInfo}),
	# url(r'^team/$', 'base_display', {'template':'team.htm', 'extra_context':{'course_list': views.get_course_list()}}),
	# url(r'^about/$', 'base_display', {'template':'about.htm', 'extra_context':{'course_list': views.get_course_list()}}),
	# url(r'^notice/$', 'base_display', {'template':'notice.htm', 'extra_context':{'course_list': views.get_course_list()}}),
	url(r'^team/$', 'base_display', {'template_name':'team.htm'}),
	url(r'^about/$', 'base_display', {'template_name':'about.htm'}),
	url(r'^notice/$', 'base_display', {'template_name':'notice.htm'}),
	url(r'^class/(\d{0,2})/$', 'class_info'),
	url(r'^focus/(\d{0,2})/$','focus'),
	url(r'^signup/$','check_signup'),
	url(r'^liuyan/(?P<lid>\d{0,4})/$', 'liuyan', {'model':models.DyCourseNews, 'GET':views.liuyan_get, 'POST':views.liuyan_post}),
    url(r'^liuyan/(?P<lid>\d{0,4})/(?P<last_liuyan_id>\d{0,4})/$', 'test_liuyan_post', {'model':models.DyCourseNews}),
	url(r'^thanks/$', 'thanks'),
	)