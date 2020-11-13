from django.db.models.signals import pre_delete
from django.dispatch import receiver

from ..models import Post, Comment, SubComment, IdCode

@receiver(pre_delete, sender=Post)
def delete_post(sender, instance, **kwargs):
    id_code = IdCode.objects.filter(code=instance.id_code).first()
    id_code.delete()

@receiver(pre_delete, sender=Comment)
def delete_comment(sender, instance, **kwargs):
    subcomments = SubComment.objects.filter(comment_id_code = instance.id_code)
    for subcomment in subcomments:
        subcomment.delete()
    id_code = IdCode.objects.filter(code=instance.id_code).first()
    id_code.delete()
    
