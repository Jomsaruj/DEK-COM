from django.db.models import Q
from .tag import Tag
from .blog import Blog


class TagManager:

    @classmethod
    def get_tag(cls, _tag_name):
        tag_name = _tag_name.lower()
        tag = Tag.objects.filter(name=tag_name).first()
        if not tag:
            tag = Tag(name=tag_name)
            print("Create new tag")
            tag.save()
        return tag

    @classmethod
    def update_tag_num(cls, _tag_name):
        tag_name = _tag_name.lower()
        tag = Tag.objects.filter(name=tag_name).first()
        num = Blog.objects.filter(Q(Post___tags__in = [tag]) | Q(Question___tags__in = [tag]) | Q(Poll___tags__in = [tag]) | Q(Job___tags__in = [tag])).count()
        if num == 0:
            tag.delete()
        else:
            tag.post_num = num
            tag.save()

