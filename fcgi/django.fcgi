#!/usr/bin/python

import sys, os


_PRJ_PATH = os.path.dirname(os.path.abspath(__file__))
_PRJ_PATH = os.path.normpath(_PRJ_PATH + '/..')
_PRJ_PATH2 = os.path.normpath(_PRJ_PATH + '/..')
#print "dirname: %s" % (_PRJ_PATH, )
_PRJ_NAME = os.path.split(_PRJ_PATH)[-1]
#print "prj_name: %s" % (_PRJ_NAME,)

#sys.stderr.write("prj_path: " + _PRJ_PATH)

# Add the project directory into python path
sys.path.insert(0, _PRJ_PATH2)
sys.path.insert(0, _PRJ_PATH)

# Switch to project directory
os.chdir(_PRJ_PATH)

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = _PRJ_NAME + '.settings'

# from django.core.servers.fastcgi import runfastcgi
#runfastcgi(method="threaded", daemonize="false")

from django.core.handlers.wsgi import WSGIHandler


_application = WSGIHandler()


def application(environ, start_response):
	environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']

	return _application(environ, start_resposne)


