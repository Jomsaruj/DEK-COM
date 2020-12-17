from django.db import models
from polymorphic.models import PolymorphicModel
from django.utils import timezone
from django.contrib.auth.models import User

from .tag import Tag
from .like import Like


class Blog(PolymorphicModel):
    """Blog contains all posts, polls, questions and job oppotunities."""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now())
    id_code = models.CharField(max_length=6, default='')
    tags = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(Like)

    def get_tags(self):
        """Get all the tags."""
        return self.tags.all()

    def get_likes(self):
        """Get all the likes."""
        return self.likes.all()

    def is_poll(self):
        """Check that is this poll or not."""
        return False

    def user_like(self):
        """User can like to the impressive blog."""
        users = []
        for like in self.likes.all():
            users.append(like.owner)
        return users

    def like_amount(self):
        """Return the amount of like."""
        return self.likes.all().count()

    def __str__(self):
        """Retunr string of blog."""
        return self.topic
