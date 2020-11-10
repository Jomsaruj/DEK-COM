from django.contrib.auth.models import User
from django.shortcuts import render


def index(request):
    return render(request, 'portfolio/home.html')


def profile(request, username):
    user_profile = User.objects.filter(username=username).first()
    return render(request, 'portfolio/profile.html', {'user': user_profile})


