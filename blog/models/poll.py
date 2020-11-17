import datetime
import random
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from .blog import Blog
from .tag import Tag


class Choice(models.Model):
    content= models.CharField(max_length = 200)
    color = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    all_votes = models.IntegerField(default = 0)
    poll_id_code = models.CharField(max_length=6, default='')
    id_code = models.CharField(max_length=6, default='')

    def get_vote_percent(self):
        if self.all_votes > 0:
            return self.votes / self.all_votes * 100
        return 0

    def get_html_bar(self):
        if self.votes > 0:
            return ('<div style="margin-bottom: 5px;height: 20px;width: ' + str(self.get_vote_percent()-10) + '%;background-color: ' + self.color + ';' + '">' + str(self.votes) + ' vote</div>')
        else:
            return ('<div style="margin-bottom: 5px;height: 20px;width: 2%;background-color: ' + self.color + ';' + '"></div>')

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

    def top_choice(self):
        return self.get_choices()[:2]

    def is_poll(self):
        return True

    def __str__(self):
        return self.topic


class Vote(models.Model): 
    question = models.ForeignKey(Poll, on_delete=models.CASCADE, default=1)
    choice = models.ForeignKey(Choice,on_delete=models.CASCADE)
    voter = models.ForeignKey(User,on_delete=models.CASCADE)
