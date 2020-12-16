from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Blog
from blog.models.like import Like


class BlogMolTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("mo")
        self.user.save()
        self.blog = Blog.objects.create(author=self.user, topic='test', id_code='123456')

    def test_like_amount(self):
        self.assertEqual(0, self.blog.like_amount())
        user1 = User.objects.create_user("ma")
        user2 = User.objects.create_user("me")
        like1 = Like.objects.create(owner=user1)
        self.blog.likes.add(like1)
        self.blog.save()
        self.assertEqual(1, self.blog.like_amount())
        like2 = Like.objects.create(owner=user2)
        self.blog.likes.add(like2)
        self.blog.save()
        self.assertEqual(2, self.blog.like_amount())

    def test_is_poll(self):
        self.assertFalse(self.blog.is_poll())

