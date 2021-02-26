from django.db import models

# Create your models here.
class News(models.Model):
    name= models.CharField(max_length=150)
    show_txt = models.TextField(default='-')
    body_txt = models.TextField(default='-')
    writer = models.CharField(max_length=30)
    picname = models.TextField(default='-')
    picurl = models.TextField(default='-')
    date = models.CharField(max_length=30, default='.')
    time = models.CharField(max_length=30, default='00:00:00')
    show=models.IntegerField(default=0)
    cat_name=models.CharField(max_length=30, default='-')
    cat_id = models.IntegerField(default=0)
    ocat_id = models.IntegerField(default=0)
    act=models.IntegerField(default=0)

    def __str__(self):
        return self.name + "|" + str(self.pk)


