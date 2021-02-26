from django.db import models

# Create your models here.
class Trending(models.Model):
    txt=models.CharField(max_length=200)

