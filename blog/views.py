from django.shortcuts import render, redirect,reverse
from django.views import generic
from .models import Post, Comment
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def blog(request):
    most_recent_post = {'most_recent_post': Post.objects.all()}
    return render(request, 'blog/blog_index.html', most_recent_post)

def go_to_blog(request):
    return redirect('blog/')

@login_required
def create_blog(request):
    if request.method == 'POST':
        topic = request.POST['post topic']
        content = request.POST['post content']
        Post.objects.create(post_topic=topic, post_content=content, author=request.user)
        return redirect(reverse('blog:blog-index'))
    return render(request, 'blog/create_blog.html')

def blog_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post).order_by('-like')
    if request.method == 'POST':
        content = request.POST['comment text']
        Comment.objects.create(content=content, post=post, author = request.user)
        return render(request, 'blog/blog_detail.html', {'post': post, 'comments': comments})
    return render(request, 'blog/blog_detail.html', {'post': post, 'comments': comments})
