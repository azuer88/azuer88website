#!/usr/bin/python
import os, sys

_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.insert(0, _PROJECT_DIR)
sys.path.insert(0, os.path.dirname(_PROJECT_DIR))
sys.path.insert(0, '/home/azuer88/modules/django-tagging')
sys.path.insert(0, '/home/azuer88/modules')

_PROJECT_NAME = _PROJECT_DIR.split('/')[-1]

#print "Project Dir: %s" % _PROJECT_DIR
#print "Project Name: %s" % _PROJECT_NAME

os.environ['DJANGO_SETTINGS_MODULE'] = "%s.settings" % _PROJECT_NAME

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
