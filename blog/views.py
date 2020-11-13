from django.shortcuts import render, redirect,reverse
from django.views import generic
from django.contrib import messages
from .models import Post, Comment, SubComment, Tag, IdCode
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models.id_code import IdCode
from .models.tag_manager import TagManager
from .models.id_code_manager import IdCodeManager

def blog(request):
    all_tag = Tag.objects.all().order_by('-post_num')
    for tag in all_tag:
        TagManager.update_tag_num(tag.name)
    selected_tags = Tag.objects.filter(active_status=True)
    if Tag.objects.filter(active_status=True).count() > 0:
        most_recent_post = Post.objects.filter(tags__in=selected_tags)
    else:
        most_recent_post = Post.objects.all()
    return render(request, 'blog/blog_index.html', {'most_recent_post': most_recent_post, 'popular_tag': all_tag, 'selected_tags': selected_tags})

def go_to_blog(request):
    return redirect('blog/')

@login_required
def create_blog(request):
    if request.method == 'POST':
        topic = request.POST['post topic']
        content = request.POST['post content']
        post = Post(post_topic=topic, post_content=content, author=request.user, id_code=IdCodeManager.get_new_id())
        comments = Comment.objects.filter(post=post).order_by('-like')
        post.save()
        for key in request.POST:
            if "tag" in key:
                tag = request.POST[key]
                if tag.strip():  # If tag are empty string just ignore it.
                    new_tag = TagManager.get_tag(tag)
                    post.tags.add(new_tag)
                    post.save()
                    TagManager.update_tag_num(new_tag.name)
        return redirect(reverse('blog:blog-detail', args=[post.id_code]))
    return render(request, 'blog/create_blog.html')

def edit_blog(request, post_id_code):
    post = Post.objects.get(id_code=post_id_code)
    comments = Comment.objects.filter(post=post).order_by('-like')
    if request.user != post.author:
        return redirect(reverse('blog:blog-detail', args=[post.id_code]))
    if request.method == 'POST':
        post.post_topic = request.POST['post topic']
        post.post_content = request.POST['post content']
        post.pub_date = timezone.now()
        post.save()
        return redirect(reverse('blog:blog-detail', args=[post.id_code]))
    return render(request, 'blog/edit_blog.html', {'post': post})

def delete_blog(request, post_id_code):
    post = Post.objects.filter(id_code=post_id_code).first()
    if request.user == post.author:
        comments = Comment.objects.filter(post=post)
        for comment in comments:
            comment.delete()
        post.delete()
        messages.warning(request, f'Post deleted!!')
    return redirect(reverse('blog:blog-index'))

def blog_detail(request, post_id_code):
    post = Post.objects.get(id_code=post_id_code)
    comments = Comment.objects.filter(post=post).order_by('-like')
    return render(request, 'blog/blog_detail.html', {'post': post, 'comments': comments})

def create_comment(request, post_id_code):
    post = Post.objects.get(id_code=post_id_code)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            path = request.path
            return redirect('/login/?next='+path)
        content = request.POST['comment text']
        Comment.objects.create(content=content, post=post, author = request.user, id_code=IdCodeManager.get_new_id())
    comments = Comment.objects.filter(post=post).order_by('-like')[:10]
    return render(request, 'blog/blog_detail.html', {'post': post, 'comments': comments})

def delete_comment(request, comment_id_code):
    comment = Comment.objects.get(id_code=comment_id_code)
    post = comment.post
    if request.user == comment.author:
        comment.delete()
        sub_comments = SubComment.objects.filter(comment_id_code=comment_id_code)
        for sub in sub_comments:
            sub.delete()
    return redirect(reverse('blog:blog-detail', args=[post.id_code]))

def create_subcomment(request, comment_id_code):
    comment = Comment.objects.get(id_code=comment_id_code)
    post = comment.post
    if request.method == 'POST':
        if not request.user.is_authenticated:
            path = request.path
            return redirect('/login/?next='+path)
        content = request.POST['subcomment text']
        SubComment.objects.create(content=content, comment_id_code=comment_id_code, author=request.user)
    return redirect(reverse('blog:blog-detail', args=[post.id_code]))

def tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    tag.active_status = not tag.active_status
    tag.save()
    return redirect(reverse('blog:blog-index'))
    