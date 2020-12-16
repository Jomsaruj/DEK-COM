from django.contrib.auth.models import User
from django.shortcuts import render, redirect,reverse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from users.models import Coin
from ..models import Blog, Post, Question, Poll, Comment, Tag, Like
from ..models.tag_manager import TagManager
from .post_views import *
from .question_views import *
from .poll_views import *
from .job_views import *


def blog(request):
    all_tag = Tag.objects.all().order_by('-post_num')[:8]
    search_post = request.GET.get('search')

    tag_filter = request.GET.getlist('tag')

    if search_post:
        most_recent_post = Blog.objects.filter(Q(topic__icontains=search_post)
                                        or Q(content__icontains=search_post)
                                        or Q(body__icontains=search_post))
        return render(request, 'blog/blog_index.html', {'most_recent_post': most_recent_post, 'popular_tag': all_tag},)
    for tag in all_tag:
        TagManager.update_tag_num(tag.name)
    
    selected_tags = Tag.objects.filter(name__in=tag_filter)
    
    if selected_tags.count() > 0:
        most_recent_post = Blog.objects.filter(
            Q(Post___tags__in=selected_tags) | 
            Q(Question___tags__in=selected_tags) | 
            Q(Job___tags__in=selected_tags) | 
            Q(Poll___tags__in=selected_tags))
    else:
        most_recent_post = Blog.objects.all()
    return render(request, 'blog/blog_index.html', {'most_recent_post': most_recent_post, 'popular_tag': all_tag, 'selected_tags': selected_tags})

def filter_blog(request, blog_type):
    all_tag = Tag.objects.all().order_by('-post_num')[:8]
    tag_filter = request.GET.getlist('tag')

    for tag in all_tag:
        TagManager.update_tag_num(tag.name)
    selected_tags = Tag.objects.filter(name__in=tag_filter)

    if blog_type == "post":
        most_recent_post = Blog.objects.instance_of(Post)
    elif blog_type == "question":
        most_recent_post = Blog.objects.instance_of(Question)
    elif blog_type == "poll":
        most_recent_post = Blog.objects.instance_of(Poll)
    elif blog_type == "job":
        most_recent_post = Blog.objects.instance_of(Job)

    if selected_tags.count() > 0:
        most_recent_post = most_recent_post.filter(tags__in=selected_tags)

    return render(request, 'blog/blog_index.html', {'most_recent_post': most_recent_post, 'popular_tag': all_tag, 'selected_tags': selected_tags})

def go_to_blog(request):
    return redirect('blog/')

@login_required
def create_blog(request, blog_type):
    template = "blog/create_" + blog_type + ".html"
    if request.method == 'POST':
        if blog_type == "post":  # if i use dict lambda it will cause multiple generate id_code
            blog = create_post(request)
        elif blog_type == "question":
            blog = create_question(request)
        elif blog_type == "poll":
            blog = create_poll(request)
        elif blog_type == "job":
            blog = create_job(request)

        if blog.topic.strip() == "":
            print("empty topic")
            messages.warning(request, f'Topic cannot be empty!!')
            return render(request, template)
 
        for key in request.POST:
            if "tag" in key:
                tag = request.POST[key]
                if tag.strip():  # If tag are empty string just ignore it.
                    new_tag = TagManager.get_tag(tag)
                    blog.tags.add(new_tag)
                    blog.save()
                    TagManager.update_tag_num(new_tag.name)
        return redirect(reverse('blog:blog-detail', args=[blog.id_code]))
    return render(request, template)

def edit_blog(request, post_id_code):
    blog = get_blog_from_id_code(post_id_code)
    blog_type = blog.__class__.__name__.lower()
    comments = Comment.objects.filter(post=blog).order_by('-like')
    if request.user != blog.author:
        return redirect(reverse('blog:blog-detail', args=[blog.id_code]))

    if blog_type == 'poll':
            return redirect(reverse('blog:blog-detail', args=[blog.id_code]))

    if request.method == 'POST':
        if blog_type in ['post', 'question']:
            edit_post(request, blog)
        elif blog_type == 'job':
            edit_job(request, blog)
        return redirect(reverse('blog:blog-detail', args=[blog.id_code]))
    return render(request, 'blog/edit_' + blog_type + '.html', {'post': blog})

def delete_blog(request, post_id_code):
    blog = get_blog_from_id_code(post_id_code)
    if request.user == blog.author or request.user.is_superuser:
        blog.delete()
        messages.warning(request, f'Post deleted!!')
    else:
        return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    return redirect(reverse('blog:blog-index'))

def blog_detail(request, id_code):
    blog = get_blog_from_id_code(id_code)
    comments = Comment.objects.filter(post=blog).order_by('-like')
    template = "blog/" + (blog.__class__.__name__).lower() + "_detail.html"
    return render(request, template, {'blog': blog, 'comments': comments})

def get_blog_from_id_code(id_code):
    return Blog.objects.filter(Q(Post___id_code=id_code) | Q(Question___id_code=id_code) | Q(Job___id_code=id_code) | Q(Poll___id_code=id_code)).first()

@login_required
def like(request, id):
    user = request.user
    post = get_blog_from_id_code(id)
    post_user = post.author
    if user.username == post_user.username:
        return redirect(reverse('blog:blog-index'))
    post_user.profile.give_coin(post, 1)
    for tag in post.get_tags():
        for coin in coins:
            if tag.name == coin.type_coin:
                coin.total_coin += 1
                coin.save()
                coin_this_type = True
        if not coin_this_type:
            new_coin = Coin.objects.create(type_coin=tag.name, total_coin=1)
            new_coin.save()
            post_user.profile.coins.add(new_coin)
        else:
            coin_this_type = False

    like = post.likes.filter(owner=user).first()
    if not like:
        like = Like(owner=user)
        like.save()

    post.likes.add(like)
    post.save()

    return redirect(reverse('blog:blog-index'))
