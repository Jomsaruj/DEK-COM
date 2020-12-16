from django.shortcuts import render, redirect,reverse

from ..models import Comment, SubComment, Question
from .blog_views import get_blog_from_id_code
from ..models.id_code import IdCode
from ..models.id_code_manager import IdCodeManager


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
        comment.author.profile.give_coin(question, -5)
        question.solution_id_code = ''
        question.save()
    else:
        question.is_closed = True
        comment.author.profile.give_coin(question, 5)
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