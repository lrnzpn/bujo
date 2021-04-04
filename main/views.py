from django.shortcuts import render, redirect
from django.views import View 
from django.core.files.storage import FileSystemStorage

from .models import MyName, Profile, Key, ThisWeek, Today
from .forms import MyNameForm, KeyForm, ThisWeekForm, TodayForm

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

            return redirect('home')
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
            renders the profile.html template,
            passing the context data to the template 
    """
    
    if not Profile.objects.exists():
        user = Profile()
        user.profile_pic = None
        user.profile_nickname = 'Your Nickname'
        user.profile_bio = 'A short description about yourself'
        user.save()
        
    user = Profile.objects.get(id=1)
    
    if response.method == 'POST':
        if response.FILES.get('profile_pic') is not None:
            file = response.FILES['profile_pic']
            fs = FileSystemStorage()
            user = Profile.objects.get(id=1)
            user.profile_pic = fs.save(file.name, file)
            user.save()
            return redirect('profile')
    
    context = {
        'user':user
    }
    return render(response, "pages/profile.html", context)

def edit_profile(response):
    """Renders the edit_profile page
    
    Args:
        response: HTTP response
    
    Returns:
        render(response, "pages/edit_profile.html", context):
            renders the edit_profile.html template,
            which makes the user able to edit the name and bio
    """
    user = Profile.objects.get(id=1)
    if response.method == 'POST':
        user.profile_nickname = response.POST.get('profile_nickname')
        user.profile_bio = response.POST.get('profile_bio')
        user.save()
        
        return redirect('profile')
        
    return render(response, 'pages/edit_profile.html', {'user':user})


def key(response):
    """Renders the key page
    
    Args:
        response: HTTP response
    
    Returns:
        render(response, "pages/key.html", context):
            renders the key.html template,
            which lets users create new keys with 
            their descriptions
    """
    if response.method == 'POST':
        
        form = KeyForm(response.POST)
        if form.is_valid():
            key = Key()
            key.key = form.cleaned_data['key']
            key.description = form.cleaned_data['description']
            key.profile_id = Profile.objects.get(id=1).id
            key.save()
            return redirect('key')
    else:
        form = KeyForm()
    
    keys = Key.objects.all()
    
    context = {
        'form': form,
        'keys': keys,
    }
    return render(response, "pages/key.html", context)


def this_week(response):
    """Renders the this_week page containing the date range of the week
    
    Args:
        response: HTTP response
    
    Returns:
        render(response, "pages/this_week.html", context):
            renders the this_week.html template,
            and gives the ability to create, edit, 
            and delete tasks, as well as mark tasks done
    """
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(6)
        
    if response.method == 'POST':
        form = ThisWeekForm(response.POST)
        if form.is_valid() and response.POST.get('add'):
            this_week = ThisWeek()
            this_week.key = Key.objects.get(id=response.POST.get('key'))
            this_week.details = form.cleaned_data['details']
            this_week.complete = False
            this_week.start_week = start_week
            this_week.end_week = end_week
            this_week.save()
            return redirect('this_week')
        
        elif response.POST.get('update'):
            task = ThisWeek.objects.get(id=response.POST.get('edit_id'))
            task.key = Key.objects.get(id=response.POST.get('key_'+str(task.id)))
            task.details = response.POST.get('details_'+str(task.id))
            task.save()
            return redirect('this_week')
        
        elif response.POST.get('delete'):
            task = ThisWeek.objects.get(id=response.POST.get('del_id'))
            task.delete()
            return redirect('this_week')
        
        elif response.POST.get('done'):
            task = ThisWeek.objects.get(id=response.POST.get('done_id'))
            task.complete = True
            task.save()
            return redirect('this_week')
    else:
        form = ThisWeekForm()
        
    tasks = ThisWeek.objects.all()
    keys = Key.objects.all()
    context = {
        'start_week': start_week.strftime('%m.%d.%a'),
        'end_week': end_week.strftime('%m.%d.%a'),
        'form': form,
        'tasks': tasks,
        'keys': keys,
    }
    
    return render(response, "pages/this_week.html", context)


def today(response):
    """Renders the today page
    
    Args:
        response: HTTP response
    
    Returns:
        render(response, "pages/today.html", context):
            renders the today.html template, 
            and gives the ability to create, edit, 
            and delete tasks, as well as mark tasks done
    """
    date = datetime.date.today()
    
    if response.method == 'POST':
        form = TodayForm(response.POST)
        if form.is_valid() and response.POST.get('add'):
            today = Today()
            today.key = Key.objects.get(id=response.POST.get('key'))
            today.details = form.cleaned_data['details']
            today.complete = False
            today.today = date
            today.save()
            return redirect('today')
        
        elif response.POST.get('update'):
            task = Today.objects.get(id=response.POST.get('edit_id'))
            task.key = Key.objects.get(id=response.POST.get('key_'+str(task.id)))
            task.details = response.POST.get('details_'+str(task.id))
            task.save()
            return redirect('today')
        
        elif response.POST.get('delete'):
            task = Today.objects.get(id=response.POST.get('del_id'))
            task.delete()
            return redirect('today')
        
        elif response.POST.get('done'):
            task = Today.objects.get(id=response.POST.get('done_id'))
            task.complete = True
            task.save()
            return redirect('today')
    else:
        form = TodayForm()
        
    tasks = Today.objects.all()
    keys = Key.objects.all()
    context = {
        'today': date,
        'form': form,
        'tasks': tasks,
        'keys': keys,
    }
    
    return render(response, "pages/today.html", context)