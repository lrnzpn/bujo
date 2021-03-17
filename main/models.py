from django.db import models

# Create your models here.
class MyName(models.Model):
    name = models.TextField(max_length=200,blank=True,null=True)

    