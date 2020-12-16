from django.urls import path

from . import views

app_name = 'portfolio'
urlpatterns = [
    path('search/', views.index, name='search'),
    path('<username>/profile', views.profile, name='profile'),
]
