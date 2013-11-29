from django.conf.urls import patterns, url
from views import RegisterView

urlpatterns = patterns('',
	url(r'^$', 'wxrobot.views.index'),
	url(r'^register/$', RegisterView.as_view(), name='register'),
	url(r'^register/add/$', 'wxrobot.views.add_register'),
)