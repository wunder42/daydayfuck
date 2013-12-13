from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views import GitItem, T

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='index'),
    url(r'^item/(?P<gid>[\w\d-]+)/$',\
     GitItem.as_view(template_name='gititem.html'), name='item'),
    url(r'^t/$', T.as_view(), name='test'),
)
