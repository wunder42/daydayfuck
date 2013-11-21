import os
import sys

root = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(root, 'site-packages'))

import sae
from dianyi import wsgi

application = sae.create_wsgi_app(wsgi.application)

# def app(environ, start_response):
#     status = '200 OK'
#     response_headers = [('Content-type', 'text/plain')]
#     start_response(status, response_headers)
#     return ['Hello, world!']

# application = sae.create_wsgi_app(app)