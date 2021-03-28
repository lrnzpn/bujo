from django.shortcuts import render
from django.views import View 
from django.http import HttpResponseRedirect

from .models import MyName, Profile
from .forms import MyNameForm, ProfileForm

import datetime


def home(response):
    """Renders the home page
    
    Args:
        response: HTTP response
    
    Returns:
        render(response, "pages/home.html", context):
            renders the home.html template, 
            passing the context data to the template 
    """
    
    if response.method == 'POST':
        form = MyNameForm(response.POST)
        if form.is_valid():
            user = MyName()
            user.name = form.cleaned_data['name']
            user.save()

            return HttpResponseRedirect('/home/')
    else:
        form = MyNameForm()
        name = None
    
    name = MyName.objects.all().last().name
    
    context = {
        'form': form,
        'name': name,
    }
    
    return render(response, "pages/home.html", context)


def profile(response):
    """Renders the profile page
    
    Args:
        response: HTTP response
    
    Returns:
        render(response, "pages/profile.html", context):
            renders the profile.html template
    """
    
    if not Profile.objects.exists():
        user = Profile()
        user.profile_pic = None
        user.profile_nickname = 'Your Nickname'
        user.profile_bio = 'A short description about yourself'
        user.save()
    
    user = Profile.objects.get(id=1)
    
    context = {
        'user':user
    }
    return render(response, "pages/profile.html", context)

def edit_profile(response):
    user = Profile.objects.get(id=1)
    form = ProfileForm(response.POST)
    if response.method == 'POST':
        user.profile_nickname = response.POST.get('profile_nickname')
        user.profile_bio = response.POST.get('profile_bio')
        user.save()
        
        return HttpResponseRedirect('/profile/')
        
    return render(response, 'pages/edit_profile.html', {'user':user})


def key(response):
    """Renders the key page
    
    Args:
        response: HTTP response
    
    Returns:
        render(response, "pages/key.html", context):
            renders the key.html template
    """
    return render(response, "pages/key.html", {})


def this_week(response):
    """Renders the this_week page containing the date range of the week
    
    Args:
        response: HTTP response
    
    Returns:
        render(response, "pages/this_week.html", context):
            renders the this_week.html template,
            passing the context data containing the starting date 
            of the week and the ending date of the week
    """
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(6)
    
    context = {
        'start_week': start_week.strftime('%m.%d.%a'),
        'end_week': end_week.strftime('%m.%d.%a'),
    }
    
    return render(response, "pages/this_week.html", context)


def today(response):
    """Renders the today page
    
    Args:
        response: HTTP response
    
    Returns:
        render(response, "pages/today.html", context):
            renders the today.html template, 
            passing the context data containing today's date
    """
    date = datetime.date.today()
    
    context = {
        'today': today,
    }
    
    return render(response, "pages/today.html", context)