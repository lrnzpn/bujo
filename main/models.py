from django.db import models
from django.utils import timezone


class MyName(models.Model):
    """MyName class creates a char field to store the user's name from the form
    """
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        """This method sets the object model name as the name that is stored
        
        Returns:
            self.name (str): name of the object stored
        """
        return self.name
   
    
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='images/')
    profile_nickname = models.CharField(max_length=40)
    profile_bio = models.TextField()
    
    def __str__(self):
        return self.profile_nickname
    
    
class Key(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.key
    
class ThisWeek(models.Model):
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    details = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    start_week = models.DateField(blank=True, null=True)
    end_week = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.details
    
class Today(models.Model):
    key = models.ForeignKey(Key, on_delete=models.CASCADE) 
    details = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    today = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.details