from django.db import models

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
    