from django.shortcuts import render
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'portfolio/home.html')


def login(request):
    return render(request, 'portfolio/login.html')
    
    
def signup(request):
    return render(request, 'portfolio/signup.html')


def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'portfolio/home.html')
    else:
        return render(request, 'portfolio/signup.html')
