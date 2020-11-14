from .tag import Tag
from . post import Post


class TagManager:

    @classmethod
    def get_tag(cls, _tag_name):
        tag_name = _tag_name.lower()
        tag = Tag.objects.filter(name=tag_name).first()
        if not tag:
            tag = Tag(name=tag_name)
            tag.save()
        return tag

    @classmethod
    def update_tag_num(cls, _tag_name):
        tag_name = _tag_name.lower()
        tag = Tag.objects.filter(name=tag_name).first()
        num = Post.objects.filter(tags__in = [tag]).count()
        if num == 0:
            tag.delete()
        else:
            tag.post_num = num
            tag.save()

