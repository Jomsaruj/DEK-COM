from django.contrib import admin
from .models import Post, Comment, SubComment, Tag

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(SubComment)
admin.site.register(Tag)

