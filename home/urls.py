from django.conf.urls.defaults import *

from views import index, static_path, disclaimer

urlpatterns = patterns('',
    (r'test/$', static_path),
    url(r'^disclaimer/$', disclaimer, name="home_disclaimer"),
    url(r'', index, name='home'),
)
