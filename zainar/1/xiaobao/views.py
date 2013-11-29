# Create your views here.
#!/usr/bin/python
# _*_ coding: UTF-8 _*_

from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
	return HttpResponse("zainar index page.")