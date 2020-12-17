from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from .blog import Blog
from .tag import Tag


class Job(Blog):
    """Job oppotunities for all user."""

    content = models.CharField(max_length=200)
    link = models.CharField(max_length=200, default='')
    requirement = models.CharField(max_length=200)
    candidates = models.ManyToManyField(User)

    def has_content(self):
        """Return the content of the blog."""
        return not len(self.content) == 0

    def has_link(self):
        """Check that has link or not."""
        return len(self.link.strip()) > 0

    def get_candidates(self):
        """Get the candidate of the person who want to find the job."""
        return self.candidates.all()

    def __str__(self):
        """Return the string."""
        return self.topic
