from django.db import models

# Create your models here.
class MyName(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name