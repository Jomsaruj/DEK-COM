from django.db import models
from django.contrib.auth.models import User


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.CharField(max_length=6, default='')