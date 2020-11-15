from django.db import models

from .blog import Blog
from .tag import Tag


class Question(Blog):
    content = models.CharField(max_length=200)
    is_closed = models.BooleanField(default=False)
    solution_id_code = models.CharField(max_length=6, default='')

    def has_content(self):
        return not len(self.content) == 0

    def __str__(self):
        return self.topic

    
