import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from .blog import Blog
from .tag import Tag


class Choice(models.Model):
    content= models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.content


class Poll(Blog):
    content = models.CharField(max_length=200)
    choices = models.ManyToManyField(Choice)
    end_date = models.DateTimeField(default=timezone.now()+datetime.timedelta(days = 7))

    def has_content(self):
        return True

    def get_choices(self):
        return self.choices.all()

    def __str__(self):
        return self.topic


class Vote(models.Model): 
    question = models.ForeignKey(Poll, on_delete=models.CASCADE, default=1)
    choice = models.ForeignKey(Choice,on_delete=models.CASCADE)
    voter = models.ForeignKey(User,on_delete=models.CASCADE)
