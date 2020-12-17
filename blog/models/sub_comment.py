from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class SubComment(models.Model):
    """Sub comment for each comment."""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now())
    comment_id_code = models.CharField(max_length=6, default='')

    def set_text(self, new_text: str):
        """Set the text for the comment."""
        self.content = new_text

    def __str__(self):
        """Return the string of the comment."""
        return self.content
