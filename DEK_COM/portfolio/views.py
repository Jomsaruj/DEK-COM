from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login


def index(request):
    return render(request, 'portfolio/home.html')


def login(request):
    return render(request, 'portfolio/login.html')
    
    
def signup(request):
    return render(request, 'portfolio/signup.html')


def signin(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return render(request, 'portfolio/home.html')
    else:
        return render(request, 'portfolio/signup.html')

