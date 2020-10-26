from django.db import models
from django.utils import timezone


class Post(models.Model):
    post_topic = models.CharField(max_length=100)
    post_content = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default = timezone.now())
    post_like = models.IntegerField(default=0)

    def get_like(self):
        return self.post_like

    def get_content(self):
        return self.post_content

    def get_topic(self):
        return self.post_topic

    def __str__(self):
        return self.post_topic


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    comment_like = models.IntegerField(default=0)

    def set_like(self, new_like: str):
        self.comment_like = new_like

    def set_text(self, new_text: str):
        self.comment_text = new_text

    def set_topic(self, new_topic: str):
        self.comment_topic = new_topic

    def get_like(self):
        return self.comment_like

    def get_text(self):
        return self.comment_text

    def get_topic(self):
        return self.comment_topic
    
    def __str__(self):
        return self.comment_text
