from django.db import models

# Create your models here.
class Newsletter(models.Model):
    txt=models.CharField(max_length=50)
    status = models.IntegerField(default=0)
