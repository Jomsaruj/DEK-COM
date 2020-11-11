from .tag import Tag


class TagManager:

    @classmethod
    def get_tag(cls, _tag_name):
        tag_name = _tag_name.lower()
        tag = Tag.objects.get(name=tag_name)
        if not tag:
            tag = Tag(name=tag_name)
            tag.save()
        return tag