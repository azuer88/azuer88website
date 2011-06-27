from django.db import models
import datetime

FILETYPE_CHOICES = (
    (1, 'Video'),
    (2, 'Audio'),
    (3, 'Slideshow'),
    (4, 'Archive'),
    (99, 'Other'),
)

class Item(models.Model):
    title = models.CharField(max_length=32)
    filename = models.FileField(upload_to='collection')
    filetype = models.SmallIntegerField(choices=FILETYPE_CHOICES)
    description = models.TextField(default='')
    downloads = models.PositiveIntegerField("Times Downloaded",default=0)
    pub_date = models.DateTimeField("Date Uploaded",default=datetime.datetime.today)
    private = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s" % (self.title)

    def pretty_filesize(self):
        bytes = self.filename.size
        if bytes >= 1073741824:
            return str((bytes / 1024 / 1024 / 1024)+1) + ' GB'
        elif bytes >= 1048576:
            return str((bytes / 1024 / 1024)+1) + ' MB'
        elif bytes >= 1024:
            return str((bytes / 1024)+1) + ' KB'
        elif bytes < 1024:
            return str(bytes) + ' bytes'
    @models.permalink
    def get_absolute_url(self):
        return ('collection_item', (), {
            'object_id': self.id,
            }
        )
