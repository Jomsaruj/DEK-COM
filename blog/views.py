from django.shortcuts import render, redirect,reverse
from django.views import generic
from .models import Post, Comment
from django.utils import timezone

def blog(request):
    most_recent_post = {"most_recent_post": Post.objects.filter(pub_date__lte=timezone.now())}
    print(most_recent_post)
    return render(request, 'blog/blog_index.html', most_recent_post)

def create_blog(request):
    if request.method == 'POST':
        topic = request.POST['post topic']
        content = request.POST['post content']
        Post.objects.create(post_topic=topic, post_content=content)
        print("Create blog success")
        return redirect("index")
    return render(request, 'blog/create_blog.html')

def blog_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/blog_detail.html', {'post': post})

class DetailView(generic.View):
    model = Post
    template_name = 'blog/blog_detail.html'