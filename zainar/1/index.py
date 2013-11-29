#-*- coding:utf-8 -*-
import os
import sys

root = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(1, os.path.join(root, 'site-packages'))
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'xiaobao.settings'
 
path = os.path.dirname(os.path.abspath(__file__)) + '/xiaobao'
if path not in sys.path:
    sys.path.insert(1, path)
 
from django.core.handlers.wsgi import WSGIHandler
from bae.core.wsgi import WSGIApplication
 
application = WSGIApplication(WSGIHandler())
