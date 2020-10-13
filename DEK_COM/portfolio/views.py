from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import auth
import os

# path = os.path.join('C:/Users/ASUS/bluej/ISp/New project/DEK-COM/DEK_COM/portfolio/templates/')
def index(request):
    return render(request, 'portfolio/home.html')


def login(request):
    return HttpResponse("You're looking at question.")

def auth_view(request):

    # here you get the post request username and password
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    # authentication of the user, to check if it's active or None
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            # this is where the user login actually happens, before this the user
            # is not logged in.
            auth.login(request, user)
            return ...
    else :
        return HttpResponseRedirect("Invalid username or password")

