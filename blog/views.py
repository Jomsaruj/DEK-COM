from django.shortcuts import render, redirect,reverse
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from .models import Blog, Post, Question, Comment, SubComment, Tag, IdCode
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models.id_code import IdCode
from .models.tag_manager import TagManager
from .models.id_code_manager import IdCodeManager

def blog(request):
    all_tag = Tag.objects.all().order_by('-post_num')[:8]
    for tag in all_tag:
        TagManager.update_tag_num(tag.name)
    selected_tags = Tag.objects.filter(active_status=True)
    if Tag.objects.filter(active_status=True).count() > 0:
        most_recent_post = Blog.objects.filter(Q(Post___tags__in=selected_tags) | Q(Question___tags__in=selected_tags))
    else:
        most_recent_post = Blog.objects.all()
    return render(request, 'blog/blog_index.html', {'most_recent_post': most_recent_post, 'popular_tag': all_tag, 'selected_tags': selected_tags})

def go_to_blog(request):
    return redirect('blog/')


@login_required
def create_blog(request, blog_type):
    if request.method == 'POST':
        if blog_type == "post":  # if i use dict lambda it will cause multiple generate id_code
            blog = create_post(request)
        elif blog_type == "question":
            blog = create_question(request)
            
        for key in request.POST:
            if "tag" in key:
                tag = request.POST[key]
                if tag.strip():  # If tag are empty string just ignore it.
                    new_tag = TagManager.get_tag(tag)
                    blog.tags.add(new_tag)
                    blog.save()
                    TagManager.update_tag_num(new_tag.name)
        return redirect(reverse('blog:blog-detail', args=[blog.id_code]))
    template = {
        "post": 'blog/create_post.html',
        "question": 'blog/create_question.html',
    }[blog_type]
    return render(request, template)

def create_post(request):
    topic = request.POST['post topic']
    content = request.POST['post content']
    post = Post(topic=topic, content=content, author=request.user, id_code=IdCodeManager.get_new_id())
    print("Genarated code for post")
    post.save()
    return post

def create_question(request):
    topic = request.POST['post topic']
    content = request.POST['post content']
    question = Question(topic=topic, content=content, author=request.user, id_code=IdCodeManager.get_new_id())
    print("Genarated code for question")
    question.save()
    return question


def edit_blog(request, post_id_code):
    post = get_blog_from_id_code(post_id_code)
    comments = Comment.objects.filter(post=post).order_by('-like')
    if request.user != post.author:
        return redirect(reverse('blog:blog-detail', args=[post.id_code]))
    if request.method == 'POST':
        post.topic = request.POST['post topic']
        post.content = request.POST['post content']
        post.pub_date = timezone.now()
        post.save()
        return redirect(reverse('blog:blog-detail', args=[post.id_code]))
    return render(request, 'blog/edit_blog.html', {'post': post})

def delete_blog(request, post_id_code):
    blog = get_blog_from_id_code(post_id_code)
    if request.user == blog.author:
        comments = Comment.objects.filter(post=blog)
        for comment in comments:
            comment.delete()
        blog.delete()
        messages.warning(request, f'Post deleted!!')
    return redirect(reverse('blog:blog-index'))

def blog_detail(request, id_code):
    blog = get_blog_from_id_code(id_code)
    comments = Comment.objects.filter(post=blog).order_by('-like')
    template = "blog/" + (blog.__class__.__name__).lower() + "_detail.html"
    return render(request, template, {'post': blog, 'comments': comments})

def get_blog_from_id_code(id_code):
    return Blog.objects.filter(Q(Post___id_code=id_code) | Q(Question___id_code=id_code)).first()


def create_comment(request, post_id_code):
    blog = get_blog_from_id_code(post_id_code)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            path = request.path
            return redirect('/login/?next='+path)
        content = request.POST['comment text']
        Comment.objects.create(content=content, post=blog, author = request.user, id_code=IdCodeManager.get_new_id())
    return redirect(reverse('blog:blog-detail', args=[blog.id_code]))

def delete_comment(request, comment_id_code):
    comment = Comment.objects.get(id_code=comment_id_code)
    post = comment.post
    if request.user == comment.author:
        comment.delete()
        sub_comments = SubComment.objects.filter(comment_id_code=comment_id_code)
        for sub in sub_comments:
            sub.delete()
    return redirect(reverse('blog:blog-detail', args=[post.id_code]))

def choose_solution(request, comment_id_code):
    comment = Comment.objects.get(id_code=comment_id_code)
    question = comment.post
    if question.__class__ != Question:
        return redirect(reverse('blog:blog-detail', args=[question.id_code]))
    if request.user != question.author:  
        # just add like to comment
        return redirect(reverse('blog:blog-detail', args=[question.id_code]))
    if question.solution_id_code == comment_id_code:
        question.is_closed = False
        question.solution_id_code = ''
        question.save()
    else:
        question.is_closed = True
        question.solution_id_code = comment.id_code
        question.save()
    return redirect(reverse('blog:blog-detail', args=[question.id_code]))

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
    