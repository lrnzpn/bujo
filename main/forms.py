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

class KeyForm(forms.Form):
    """KeyForm creates a form for the key name and key description
    """
    key = forms.CharField(label="Key",max_length=100,
                          widget= forms.TextInput
                           (attrs={'class':'form-control mb-3'}))
    description = forms.CharField(label="Description",max_length=255,
                          widget= forms.TextInput
                           (attrs={'class':'form-control mb-3'}))
    
    class Meta:
        model = Key
        fields = "__all__"

keys = [(k.id, k.key) for k in Key.objects.all()]

class ThisWeekForm(forms.Form):
    """ThisWeekForm creates a form containing the select field of key options
    and the task details under it
    """
    key = forms.ChoiceField(choices=keys, widget= forms.Select
                           (attrs={'class':'custom-select'}))
    details = forms.CharField(label="Details",max_length=255,
                          widget= forms.TextInput
                           (attrs={'class':'form-control mb-3'}))
    
    class Meta:
        model = ThisWeek
        fields = ['key', 'details']
        
class TodayForm(forms.Form):
    """TodayForm creates a form containing the select field of key options
    and the task details under it
    """
    key = forms.ChoiceField(choices=keys, widget= forms.Select
                           (attrs={'class':'custom-select'}))
    details = forms.CharField(label="Details",max_length=255,
                          widget= forms.TextInput
                           (attrs={'class':'form-control mb-3'}))
    
    class Meta:
        model = Today
        fields = ['key', 'details']