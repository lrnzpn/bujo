from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('key/', key, name='key'),
    path('this_week/', this_week, name='this_week'),
    path('today/', today, name='today'),
]