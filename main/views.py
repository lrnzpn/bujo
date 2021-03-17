from django.shortcuts import render
from django.views import View 
from django.http import HttpResponseRedirect

from .models import *
from .forms import *

import datetime


def home(response):
    if(response.method == 'POST'):
        form = MyName(response.POST)
        if form.is_valid():
            user = MyName()
            user.name = form.cleaned_data['name']
            user.save()
            return HttpResponseRedirect('/home/')
    else:
        form = MyName()
    
    # print(MyName.objects.all().last().name)
    return render(response, "pages/home.html", {'form':form})


def profile(response):
    return render(response, "pages/profile.html", {})


def key(response):
    return render(response, "pages/key.html", {})


def this_week(response):
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(6)
    
    context = {
        'start_week': start_week.strftime('%m.%d.%a'),
        'end_week': end_week.strftime('%m.%d.%a'),
    }
    
    return render(response, "pages/this_week.html", context)


def today(response):
    date = datetime.date.today()
    
    context = {
        'today': today,
    }
    
    return render(response, "pages/today.html", context)