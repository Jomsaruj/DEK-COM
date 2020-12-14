
from django.contrib.auth.models import User
from django.shortcuts import render
from blog.models.post import Post
from django.db.models import Q


def index(request):
    search_post = request.GET.get('search')
    if search_post:
        posts = Post.objects.filter(Q(title__icontains=search_post) | Q(content__icontains=search_post))
    return render(request, 'portfolio/profile.html', {'posts': posts})


def profile(request, username):
    user_profile = User.objects.filter(username=username).first()
    return render(request, 'portfolio/profile.html', {'user': user_profile})




