"""add path to the URL."""
from django.urls import path, include
from . import views

app_name = "portfolio"
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]
