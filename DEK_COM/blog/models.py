from django.db import models


class Post(models.Model):
    post_topic = models.CharField(max_length=100)
    post_text = models.CharField(max_length=200)
    post_like = models.IntegerField(default=0)

    def modify_post(self, new_text: str):
        self.post_text = new_text

    def __str__(self):
        return self.post_text


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    comment_like = models.IntegerField(default=0)

    def modify_comment(self, new_text: str):
        self.comment_text = new_text

    def __str__(self):
        return self.comment_text
