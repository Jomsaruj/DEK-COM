from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'portfolio/home.html')


def profile(request, username):
    return render(request, 'portfolio/profile.html')




