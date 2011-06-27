from django.db import models


FILE_CHOICES = (
    (1, 'Image'),
    (2, 'Video'),
    (3, 'Audio'),
    (4, 'Other'),
)

class File(models.Model):
    name = models.CharField(max_length=30, unique=True)
    filename = models.FileField(upload_to='files/')
    filetype = models.SmallIntegerField(choices=FILE_CHOICES)


    def __unicode__(self):
        return "%s (%s)" % (self.name, self.get_filetype_display())
