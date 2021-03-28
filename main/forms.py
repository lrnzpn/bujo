from django import forms
from .models import *

class MyNameForm(forms.Form):
    """MyNameForm creates a form containing a text input field 
    that accepts a string to be stored in the database
    """
    name = forms.CharField(label="Name", max_length=200, 
                           widget= forms.TextInput
                           (attrs={'class':'form-control w-50 mt-1 mb-3'})) # optional args

    class Meta:
        model = MyName
        fields = ['name']

class ProfileForm(forms.Form):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'custom-file-input'}))
    profile_nickname = forms.CharField(label="Nickname", max_length=40, 
                           widget=forms.TextInput
                           (attrs={'class':'form-control'}))
    profile_bio = forms.CharField(label="Bio", 
                                  widget=forms.Textarea
                           (attrs={'class':'form-control'}))
    class Meta:
        model = Profile
        fields = ['profile_nickname','profile_bio']