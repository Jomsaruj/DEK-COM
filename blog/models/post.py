from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_topic = models.CharField(max_length=100)
    post_content = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now())

    def get_topic(self):
        return self.post_topic

    def get_content(self):
        return self.post_content

    def has_content(self):
        return not len(self.post_content) == 0

    def get_pubdate(self):
        return self.pub_date

    def get_like(self):
        return self.post_like

    def __str__(self):
        return self.post_topic