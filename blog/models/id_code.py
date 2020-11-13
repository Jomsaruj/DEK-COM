from django.db import models
from better_profanity import profanity
import random, string


class IdCode(models.Model):
    code = models.CharField(max_length=6, default='')

