from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Blog, Tag
from users.models import Coin


class Coin_test(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("mark")
        self.user.save()
        self.user.profile.coins.add(Coin.objects.create(type_coin="test1", total_coin=2))
        self.user.profile.coins.add(Coin.objects.create(type_coin="test2", total_coin=3))
        self.user.profile.save()

    def test_get_total_coin(self):
        self.assertEqual(5,self.user.profile.get_total_coin())
        self.user.profile.coins.add(Coin.objects.create(type_coin="test3", total_coin=4))
        self.assertEqual(9, self.user.profile.get_total_coin())

    def test_get_total_types(self):
        self.assertEqual(2,self.user.profile.get_total_types())
        self.user.profile.coins.add(Coin.objects.create(type_coin="test3", total_coin=7))
        self.assertEqual(3, self.user.profile.get_total_types())

    def test_give_coin(self):
        blog = Blog.objects.create(author=self.user, topic="test_coin")
        blog.tags.add(Tag.objects.create(name="test1"))
        blog.save()
        self.user.profile.give_coin(blog, 1)
        self.assertEqual(2, self.user.profile.get_total_types())
        self.assertEqual(6, self.user.profile.get_total_coin())
        blog.tags.add(Tag.objects.create(name="test3"))
        blog.save()
        self.user.profile.give_coin(blog, 2)
        self.assertEqual(3, self.user.profile.get_total_types())
        self.assertEqual(10, self.user.profile.get_total_coin())

