from django.conf.urls import patterns, url
from views import RegisterView

urlpatterns = patterns('',
	url(r'^$', 'wxrobot.views.index'),
	url(r'^register/$', RegisterView.as_view(), name='register'),
	url(r'^register/add/$', 'wxrobot.views.add_register'),

	###########
	url(r'^clear_cache/$', 'wxrobot.views.clear_cache'),
	url(r'^update_jokes/$', 'wxrobot.views.update_jokes'),
	url(r'^update_weather/$', 'wxrobot.views._register_weather')
)