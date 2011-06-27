from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.auth.models import User
from django.conf import settings

from django.core.exceptions import ObjectDoesNotExist

from basic.blog.managers import PublicManager

import datetime
import tagging
from tagging.fields import TagField

import logging

#fb posting
from utils.fb import GraphAPI
from settings import FACEBOOK_ACCESS_TOKEN, HOME_URL

class Category(models.Model):
    """Category model."""
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        db_table = 'blog_categories'
        ordering = ('title',)

    def __unicode__(self):
        return u'%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('blog_category_detail', None, {'slug': self.slug})


class FBPost(models.Model):
    id = models.IntegerField(primary_key=True)
    date_posted = models.DateTimeField(_('date posted'), blank=True, null=True)

class Post(models.Model):
    """Post model."""
    STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Public')),
    )
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), unique_for_date='publish')
    author = models.ForeignKey(User, blank=True, null=True)
    body = models.TextField(_('body'), )
    tease = models.TextField(_('tease'), blank=True, help_text=_('Concise text suggested. Does not appear in RSS feed.'))
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    allow_comments = models.BooleanField(_('allow comments'), default=True)
    publish = models.DateTimeField(_('publish'), default=datetime.datetime.now)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    categories = models.ManyToManyField(Category, blank=True)
    tags = TagField()
    objects = PublicManager()

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        db_table  = 'blog_posts'
        ordering  = ('-publish',)
        get_latest_by = 'publish'

    def __unicode__(self):
        return u'%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('blog_detail', None, {
            'year': self.publish.year,
            'month': self.publish.strftime('%b').lower(),
            'day': self.publish.day,
            'slug': self.slug
        })

    def get_previous_post(self):
        return self.get_previous_by_publish(status__gte=2)

    def get_next_post(self):
        return self.get_next_by_publish(status__gte=2)
    
    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs) # Call the "real" save() method.
        
        try:
            fp = FBPost.objects.get(pk=self.pk)
            found = True
        except ObjectDoesNotExist:
            found = False
            
        if is_new:
            logging.debug('Posting a new post record, ''%s'' at %s' % (self.title,self.get_absolute_url()))
            
            if self.status == 2: # 1=Draft 2=Public 
                g = GraphAPI(FACEBOOK_ACCESS_TOKEN)
                
                att = {}
                att['Name'] = self.title
                att['link'] = HOME_URL + self.get_absolute_url()
                att['description'] = self.tease
                
                graph.put_wall_post("I posted a new article on my website.", att)
            
            else:
                logging.debug('Private post, not submitted to fb')
            
            
##>>> from settings import FB_ACCESS_TOKEN
##>>> import facebook
##>>> graph = facebook.GraphAPI(FB_ACCESS_TOKEN)
##>>> attach = {}
##>>> attach ["name"] = "Blog Post Link"
##>>> attach["link"] = "http://azuer88.alwaysdata.net/"
##>>> attach["description"] = "Blog Post at azuer88"
##>>> graph.put_wall_post("this is post from my django project/app", attach)
##{u'id': u'100002155522088_127945017287348'}            

class BlogRoll(models.Model):
    """Other blogs you follow."""
    name = models.CharField(max_length=100)
    url = models.URLField(verify_exists=False)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('sort_order', 'name',)
        verbose_name = _('blog roll')
        verbose_name_plural = _('blog roll')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return self.url