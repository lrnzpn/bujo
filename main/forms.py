from django import forms

class MyNameForm(forms.Form):
    """MyNameForm creates a form containing a text input field 
    that accepts a string to be stored in the database
    """
    name = forms.CharField(label="Name", max_length=200, 
                           widget= forms.TextInput
                           (attrs={'class':'form-control w-50 mt-1 mb-3'})) # optional args
