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

    def give_coin(self, post, total):
        for tag in post.get_tags():
            coin_this_type = False
            for coin in self.get_coins():
                if tag.name == coin.type_coin:
                    coin.total_coin += total
                    if coin.total_coin == 0:
                        coin.delete()
                    coin.save()
                    coin_this_type = True
            if not coin_this_type:
                new_coin = Coin.objects.create(type_coin=tag.name, total_coin=total)
                new_coin.save()
                self.coins.add(new_coin)
