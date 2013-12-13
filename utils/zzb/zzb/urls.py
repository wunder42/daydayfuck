from django.conf.urls import patterns, include, url

from django.contrib import admin

import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'', include('home.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',\
    	{'document_root': settings.STATIC_ROOT}),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
