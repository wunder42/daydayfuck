from django.conf.urls import patterns, include, url
from django.views.generic import FormView
from .forms import TForm

urlpatterns = patterns('', 
	url(r'', FormView.as_view(template_name='demo.html', form_class=TForm)),
)