from django.db import models

from .blog import Blog
from .tag import Tag


class Post(Blog):
    content = models.CharField(max_length=200)

    def has_content(self):
        return not len(self.content) == 0

    def __str__(self):
        return self.topic

    
