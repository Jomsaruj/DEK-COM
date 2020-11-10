from django.shortcuts import render, redirect,reverse
from django.views import generic
from django.contrib import messages
from .models import Post, Comment, SubComment
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models.tag import Tag

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

def edit_blog(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-like')
    if request.method == 'POST':
        post.post_topic = request.POST['post topic']
        post.post_content = request.POST['post content']
        post.pub_date = timezone.now()
        post.save()
        return redirect(reverse('blog:blog-detail', args=[post.id]))
    return render(request, 'blog/edit_blog.html', {'post': post})

def delete_blog(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    messages.warning(request, f'Post deleted!!')
    return redirect(reverse('blog:blog-index'))

def blog_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post).order_by('-like')
    if request.method == 'POST':
        content = request.POST['comment text']
        Comment.objects.create(content=content, post=post, author = request.user, tag=Tag.get_new_tag())
    return render(request, 'blog/blog_detail.html', {'post': post, 'comments': comments})

def create_subcomment(request, comment_tag):
    comment = Comment.objects.get(tag=comment_tag)
    post = comment.post
    if request.method == 'POST':
        content = request.POST['subcomment text']
        SubComment.objects.create(content=content, comment_tag=comment_tag, author=request.user)
    return redirect(reverse('blog:blog-detail', args=[post.id]))