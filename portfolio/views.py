from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import auth
import os

# path = os.path.join('C:/Users/ASUS/bluej/ISp/New project/DEK-COM/DEK_COM/portfolio/templates/')
def index(request):
    return render(request, 'portfolio/home.html')



