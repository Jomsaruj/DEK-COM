from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Post


class PostTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("mo")
        self.user.save()
        self.post = Post.objects.create(author=self.user, topic='test', id_code='123456', content='')

    def test_has_content(self):
        self.assertFalse(self.post.has_content())
        self.post2 = Post.objects.create(author=self.user, topic='test2', id_code='555555', content='want')
        self.assertTrue(self.post2.has_content())
