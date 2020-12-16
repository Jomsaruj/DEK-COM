import datetime
import random
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from .blog import Blog
from .tag import Tag


class Choice(models.Model):
    """Make choices for the poll."""

    content = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    all_votes = models.IntegerField(default=0)
    poll_id_code = models.CharField(max_length=6, default='')
    id_code = models.CharField(max_length=6, default='')

    def get_vote_percent(self):
        """Compute the percent of the vote."""
        if self.all_votes > 0:
            return self.votes / self.all_votes * 100
        return 0

    def get_html_bar(self):
        """Show the bar of the vote."""
        if self.votes > 0:
            return ('<div style="margin-bottom: 5px;height: 20px;width: ' + str(self.get_vote_percent()-10) + '%;background-color: ' + self.color + ';' + '"><p class="vote-score">' + str(self.votes) + ' vote</p></div>')
        else:
            return ('<div style="margin-bottom: 5px;height: 20px;width: 2%;background-color: ' + self.color + ';' + '"></div>')

    def __str__(self):
        """Return the string of poll content."""
        return self.content


class Poll(Blog):
    """Generate the poll."""

    content = models.CharField(max_length=200)
    choices = models.ManyToManyField(Choice)
    end_date = models.DateTimeField(default=timezone.now()+datetime.timedelta(days = 7))

    def has_content(self):
        """Generate the poll content."""
        return True

    def get_choices(self):
        """Get the choice of the poll."""
        return self.choices.all().order_by('-votes')

    def top_choice(self):
        """Return the top choice."""
        return self.get_choices()[:2]

    def is_poll(self):
        """Check this is poll or not."""
        return True

    def __str__(self):
        """Return the string."""
        return self.topic


class Vote(models.Model):
    """Get the vote for the poll."""
    question = models.ForeignKey(Poll, on_delete=models.CASCADE, default=1)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
