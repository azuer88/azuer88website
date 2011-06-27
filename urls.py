from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^webhome/', include('webhome.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^comments/', include('django.contrib.comments.urls')),
    # Uncomment the next line to enable the admin:
    (r'^blog/', include('basic.blog.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'^files/', include('collection.urls')),
    (r'^home/', include('home.urls')),
    #(r'^tools/', include('wtools.urls')),
    (r'^$', 'home.views.index', {}, 'home_index'),
)

# adding a robots.txt and sitemap.xml
from django.contrib.sitemaps import GenericSitemap
from basic.blog.models import Post
from collection.models import Item
post_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'publish',
}
item_dict = {
    'queryset': Item.objects.all(),
    'date_field': 'pub_date',
}
sitemaps = {
    'blog': GenericSitemap(post_dict, priority=0.6),
    'collection': GenericSitemap(item_dict, priority=0.4),
}

from django.views.generic.simple import direct_to_template
urlpatterns = patterns('',
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^robots\.txt$', direct_to_template,
     {'template': 'robots.txt', 'mimetype': 'text/plain'}),
) + urlpatterns

from settings import _PROJECT_DIR, DEBUG, MEDIA_ROOT

#if DEBUG:
if True:
    urlpatterns = patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': MEDIA_ROOT, 'show_indexes': True}),
            ) + urlpatterns



## catch-all url
if not DEBUG:
    urlpatterns += patterns('',
        (r'', 'home.views.index'),
    )
