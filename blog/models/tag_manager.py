from .tag import Tag


class TagManager:

    @classmethod
    def get_tag(cls, _tag_name):
        tag_name = _tag_name.lower()
        tag = Tag.objects.filter(name=tag_name).first()
        if not tag:
            tag = Tag(name=tag_name)
            tag.save()
        else:
            tag.post_add_tag()
        return tag

