from django.db import models

# Create your models here.
class Main(models.Model):
    name = models.CharField(max_length=30, default='.')
    about = models.TextField(default='.')
    abouttxt = models.TextField(default='.')
    fb = models.CharField(max_length=30, default='.')
    tw = models.CharField(max_length=30, default='.')
    yt = models.CharField(max_length=30, default='.')
    tell = models.BigIntegerField(default= 4466456454 )
    link = models.CharField(max_length=30, default='.')

    set_name = models.CharField(max_length=30, default='.')

    picurl = models.TextField(default='.')
    picname = models.TextField(default='')

    picurl2 = models.TextField(default='.')
    picname2 = models.TextField(default='.')

    def __str__(self):
        return self.set_name + str(self.pk)
