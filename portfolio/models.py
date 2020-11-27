from django.db import models
from django.contrib.auth.models import User

from users.models import Coin


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_image')
    cover_image = models.ImageField(default='default2.jpg', upload_to='cover_image')
    formal_image = models.ImageField(default='default2.jpg', upload_to='formal_image')
    coin = models.ManyToManyField(Coin)

    def __str__(self):
        return f'{self.user.username} profile image'

    def get_total_coin(self):
        return self.coin.all().first()

    def get_coin(self):
        return self.coin.all()


