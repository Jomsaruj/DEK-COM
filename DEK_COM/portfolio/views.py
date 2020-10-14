# from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
# from django.contrib.auth import logout
# from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect


def index(request):
    """Redirect user to DEK-COM home page"""
    return render(request, 'portfolio/home.html')


def login(request):
    """Redirect user to DEK-COM log in page"""
    return render(request, 'portfolio/login.html')
    
    
def signup(request):
    """Redirect user to DEK-COM sign up page"""
    return render(request, 'portfolio/signup.html')


def signin(request):
    """Get username and password form login.html and then log user in if valid"""
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        # This part is only for iteration1
        messages.success(request, "Hello! " + username + " You are now Log In!")
        ##################################
        return render(request, 'portfolio/home.html')
    else:
        messages.error(request, "Username or Password is incorrect")
        return redirect('portfolio:login')

# NOTE: not finish
# def signout(request):
#     """log user out"""
#     logout(request)
#     return HttpResponseRedirect(reverse('portfolio:index'))

