from django.db.models.signals import pre_delete
from django.dispatch import receiver

from ..models import Blog, Post, Question, Poll, Choice, Vote, Comment, SubComment, IdCode


@receiver(pre_delete, sender=Blog)
def delete_blog(sender, instance, **kwargs):
    comments = Comment.objects.filter(post=instance)
    for comment in comments:
        comment.delete()
    clear_choice(instance.id_code)
    id_code = IdCode.objects.filter(code=instance.id_code).first()
    id_code.delete()

@receiver(pre_delete, sender=Comment)
def delete_comment(sender, instance, **kwargs):
    subcomments = SubComment.objects.filter(comment_id_code = instance.id_code)
    for subcomment in subcomments:
        subcomment.delete()
    id_code = IdCode.objects.filter(code=instance.id_code).first()
    id_code.delete()

def clear_choice(poll_id_code):
    choices = Choice.objects.filter(poll_id_code=poll_id_code)
    for choice in choices:
        id_code = IdCode.objects.filter(code=choice.id_code).first()
        id_code.delete()
        choice.delete()

    
