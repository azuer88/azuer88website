from django.conf.urls.defaults import *


from views import index, list_items, collection_list, download_item, collection_item

urlpatterns = patterns('',
    url(r'^page/(?P<page>\d+)/$', list_items, name='list_items_paginated'),
    url(r'^page/(?P<page>\d+)/$', collection_list, name='collection_list_paginated'),
    url(r'download/(?P<object_id>\d+)/(?P<object_path>.*)$', download_item, name='download_item'),
    url(r'view/(?P<object_id>\d+)/$', collection_item, name="collection_item"),
    ('^$', index),
    # Example:
    # (r'^olles4/', include('olles4.foo.urls')),
    #  url(r'^accounts/logout/', 'django.contrib.auth.views.logout', name='auth_logout'),
)
