from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from .post import Post
from .sub_comment import SubComment

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    date = models.DateTimeField(default = timezone.now())
    like = models.IntegerField(default=0)
    id_code = models.CharField(max_length=6, default='')

    def set_text(self, new_text: str):
        self.content = new_text

    def get_like(self):
        return self.ike

    @property
    def sub_comment(self):
        return SubComment.objects.filter(comment_id_code=self.id_code)

    def __str__(self):
        return self.content