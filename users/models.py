from django.contrib.auth.models import User
from django.db import models


class Coin(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_coin = models.IntegerField(default=0)

    def get_total_coin(self):
        return self.total_coin

    def __str__(self):
        return f"{self.total_coin}"