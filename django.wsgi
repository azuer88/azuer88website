#!/usr/bin/python

import sys, os
from django.core.handlers.wsgi import WSGIHandler

# detect project path and its parent
_PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
_PARENT_PATH = os.path.normpath(_PROJECT_PATH + '/..')
_PROJECT_NAME = os.path.split(_PROJECT_PATH)[-1]

# Add the project directory and its parent into python path
sys.path.insert(0, _PARENT_PATH)
sys.path.insert(0, _PROJECT_PATH)

# Switch to project directory
os.chdir(_PROJECT_PATH)

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = _PROJECT_NAME + '.settings'

_application = WSGIHandler()

def application(environ, start_response):
# for older django, where PATH_INFO requires both script name and path info.
#	environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
	return _application(environ, start_response)


if __name__ == '__main__':
	from flup.server.fcgi import WSGIServer

	WSGIServer(application).run()
