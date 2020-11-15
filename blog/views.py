from django.shortcuts import render, redirect,reverse
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from .models import Blog, Post, Question, Job, Comment, SubComment, Tag, IdCode
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
        most_recent_post = Blog.objects.filter(Q(Post___tags__in=selected_tags) | Q(Question___tags__in=selected_tags) | Q(Job___tags__in=selected_tags))
    else:
        most_recent_post = Blog.objects.all()
    return render(request, 'blog/blog_index.html', {'most_recent_post': most_recent_post, 'popular_tag': all_tag, 'selected_tags': selected_tags})

def filter_blog(request, blog_type):
    all_tag = Tag.objects.all().order_by('-post_num')[:8]
    for tag in all_tag:
        TagManager.update_tag_num(tag.name)
    selected_tags = Tag.objects.filter(active_status=True)

    if blog_type == "post":
        most_recent_post = Blog.objects.instance_of(Post)
    elif blog_type == "question":
        most_recent_post = Blog.objects.instance_of(Question)
    elif blog_type == "job":
        most_recent_post = Blog.objects.instance_of(Job)

    if Tag.objects.filter(active_status=True).count() > 0:
        most_recent_post = most_recent_post.filter(tags__in=selected_tags)

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
        elif blog_type == "job":
            blog = create_job(request)
            
        for key in request.POST:
            if "tag" in key:
                tag = request.POST[key]
                if tag.strip():  # If tag are empty string just ignore it.
                    new_tag = TagManager.get_tag(tag)
                    blog.tags.add(new_tag)
                    blog.save()
                    TagManager.update_tag_num(new_tag.name)
        return redirect(reverse('blog:blog-detail', args=[blog.id_code]))
    template = "blog/create_" + blog_type + ".html"
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

def create_job(request):
    topic = request.POST['job topic']
    requirement = request.POST['job requirement']
    detail = request.POST['job detail']
    job = Job(topic=topic, requirement=requirement, content=detail, author=request.user, id_code=IdCodeManager.get_new_id())
    job.save()
    return job


def edit_blog(request, post_id_code):
    blog = get_blog_from_id_code(post_id_code)
    blog_type = blog.__class__.__name__.lower()
    comments = Comment.objects.filter(post=blog).order_by('-like')
    if request.user != blog.author:
        return redirect(reverse('blog:blog-detail', args=[blog.id_code]))
    if request.method == 'POST':
        if blog_type in ['post', 'question']:
            edit_post(request, blog)
        elif blog_type == 'job':
            edit_job(request, blog)
        return redirect(reverse('blog:blog-detail', args=[blog.id_code]))
    return render(request, 'blog/edit_' + blog_type + '.html', {'post': blog})

def edit_post(request, blog):
    blog.topic = request.POST['post topic']
    blog.content = request.POST['post content']
    blog.pub_date = timezone.now()
    blog.save()

def edit_job(request, job):
    job.topic = request.POST['job topic']
    job.requirement = request.POST['job requirement']
    job.content = request.POST['job detail']
    job.save()

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
    return render(request, template, {'blog': blog, 'comments': comments})

def get_blog_from_id_code(id_code):
    return Blog.objects.filter(Q(Post___id_code=id_code) | Q(Question___id_code=id_code) | Q(Job___id_code=id_code)).first()


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
    