from django.db import models
from django.contrib.auth.models import User


class Like(models.Model):
    """The like from the other user or from yourself."""

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.CharField(max_length=6, default='')