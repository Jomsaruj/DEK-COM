from django.db import models
from django.utils import timezone

from .blog import Blog
from .tag import Tag


class Job(Blog):
    content = models.CharField(max_length=200)
    link = models.CharField(max_length=200, default='')
    requirement = models.CharField(max_length=200)
    detail = models.CharField(max_length=200)

    def has_content(self):
        return not len(self.content) == 0

    def have_link(self):
        return len(self.link.strip()) > 0

    def __str__(self):
        return self.topic

    
