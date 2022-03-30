from django.db import models

# Create your models here.
class Data(models.Model):
    feature = models.IntegerField(null=True,blank=True)
    value = models.IntegerField(null=True,blank=True)