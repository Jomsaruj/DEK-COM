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
        Post.objects.create(post_topic=topic, post_content=content, user=request.user.username, auther_image=request.user.profile.image.url)
        return redirect('index')
    return render(request, 'blog/create_blog.html')

def blog_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        text = request.POST['comment text']
        post.add_comment(Comment(comment_text=text))
        return render(request, 'blog/blog_detail.html', {'post': post})
    return render(request, 'blog/blog_detail.html', {'post': post})
