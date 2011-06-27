from django.db import models

# Create your models here.
class MenuLink(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, default='')
    title = models.CharField(max_length=100, blank=False, null=False, default='')
    caption = models.CharField(max_length=100, blank=False, null=False, default='')
    active = models.BooleanField(default=True)
    sequence = models.IntegerField()
    class Meta:
        managed = True
        ordering = ['sequence', ]
    def __unicode__(self):
        return "%s (%s)" % (self.caption, self.name)
