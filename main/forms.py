from django import forms

class MyNameForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200, 
                           widget= forms.TextInput
                           (attrs={'class':'form-control w-50 mt-1 mb-3'})) # optional args
