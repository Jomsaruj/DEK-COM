from django.contrib import admin
from .models import Post, Question, Comment, SubComment, Tag, IdCode

admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(SubComment)
admin.site.register(Tag)
admin.site.register(IdCode)

