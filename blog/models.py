from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    # post_owner = get_user()
    post_topic = models.CharField(max_length=100)
    post_content = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now())
    user = models.CharField(max_length=20)
    auther_image = models.ImageField()
    post_like = 0

    def get_topic(self):
        return self.post_topic

    def get_content(self):
        return self.post_content

    def has_content(self):
        return not len(self.post_content) == 0

    def get_auther(self):
        return self.user

    def get_pubdate(self):
        return self.pub_date

    def get_like(self):
        return self.post_like

    def __str__(self):
        return self.post_topic


class Comment(models.Model):
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    comment_like = models.IntegerField(default=0)
    comment_date = models.DateTimeField(default = timezone.now())

    def set_text(self, new_text: str):
        self.comment_text = new_text

    def get_like(self):
        return self.comment_like

    def get_topic(self):
        return self.comment_topic

    def get_text(self):
        return self.comment_text

    def __str__(self):
        return self.comment_text
