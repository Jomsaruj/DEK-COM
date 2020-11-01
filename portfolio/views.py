from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import auth
import os

# path = os.path.join('C:/Users/ASUS/bluej/ISp/New project/DEK-COM/DEK_COM/portfolio/templates/')

def index(request):
    return render(request, 'portfolio/home.html')

def profile(request, username):
    user_profile = User.objects.filter(username=username).first()
    return render(request, 'portfolio/profile.html', {'user': user_profile})


