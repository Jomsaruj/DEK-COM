from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Blog, Comment


class CommentTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("mo")
        self.user.save()
        self.blog = Blog.objects.create(author=self.user, topic='test', id_code='123456')
        self.comment = Comment.objects.create(post=self.blog, author=self.user, content="test", id_code='234567')

    def test_set_text(self):
        self.assertEqual("test", str(self.comment))
        self.comment.set_text("not test")
        self.assertEqual("not test", str(self.comment))


