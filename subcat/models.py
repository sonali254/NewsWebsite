from django.db import models

# Create your models here.
class Subcat(models.Model):
    name=models.CharField(max_length=30)
    cat_name=models.CharField(max_length=30)
    cat_id=models.IntegerField()
    def __str__(self):
        return self.name