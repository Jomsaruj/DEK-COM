from django.contrib import admin
from .models import Post, Question, Poll, Choice, Vote, Job, Comment, SubComment, Tag, IdCode

admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Vote)
admin.site.register(Job)
admin.site.register(Comment)
admin.site.register(SubComment)
admin.site.register(Tag)
admin.site.register(IdCode)

