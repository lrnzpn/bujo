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
    """Profile class creates a model to store images, as well as the name
    and bio of the user
    """
    profile_pic = models.ImageField(upload_to='images/')
    profile_nickname = models.CharField(max_length=40)
    profile_bio = models.TextField()
    
    def __str__(self):
        """This method sets the object model name as the name that is stored
        
        Returns:
            self.name (str): name of the object stored
        """
        return self.profile_nickname
    
    
class Key(models.Model):
    """Key class creates a model to store key names and description,
    and is tied to the profile of the user 
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        """This method sets the object model name as the name that is stored
        
        Returns:
            self.name (str): name of the object stored
        """
        return self.key
    
class ThisWeek(models.Model):
    """ThisWeek class creates a model to store what key was selected, the details
    of the task, if the task is completed, and the start and end week dates
    """
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    details = models.CharField(max_length=255, blank=True, null=True)
    complete = models.BooleanField(default=False)
    start_week = models.DateField(blank=True, null=True)
    end_week = models.DateField(blank=True, null=True)
    
    def __str__(self):
        """This method sets the object model name as the name that is stored
        
        Returns:
            self.name (str): name of the object stored
        """
        return self.details
    
class Today(models.Model):
    """ThisWeek class creates a model to store what key was selected, the details
    of the task, if the task is completed, and date today
    """
    key = models.ForeignKey(Key, on_delete=models.CASCADE) 
    details = models.CharField(max_length=255, blank=True, null=True)
    complete = models.BooleanField(default=False)
    today = models.DateField(default=timezone.now)
    
    def __str__(self):
        """This method sets the object model name as the name that is stored
        
        Returns:
            self.name (str): name of the object stored
        """
        return self.details