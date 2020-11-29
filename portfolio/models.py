from django.db import models
from django.contrib.auth.models import User

from users.models import Coin


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_image')
    cover_image = models.ImageField(default='default2.jpg', upload_to='cover_image')
    formal_image = models.ImageField(default='default2.jpg', upload_to='formal_image')
    coins = models.ManyToManyField(Coin)

    def __str__(self):
        return f'{self.user.username} profile image'

    def get_total_coin(self):
        total = 0
        for coin in self.get_coins():
            total += coin.total_coin
        return total

    def get_coins(self):
        return self.coins.all()

    def get_total_types(self):
        return self.coins.all().count()

    def get_most_coins(self):
        list_most_coins = self.get_coins().order_by('-total_coin')[:5]
        return list_most_coins
