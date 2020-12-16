from django.db import models

from .blog import Blog
from .tag import Tag


class Post(Blog):
    """For generate the post."""

    content = models.CharField(max_length=200)

    def has_content(self):
        """Check that psot has content or not."""
        return not len(self.content) == 0

    def __str__(self):
        """Return the string of the poll."""
        return self.topic
