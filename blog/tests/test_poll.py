from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Poll

class PollTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("mo")
        self.user.save()
        self.poll = Poll.objects.create(author=self.user, topic='test', id_code='123456', content='')

    def test_has_content(self):
        self.assertTrue(self.poll.has_content())

    def test_is_poll(self):
        self.assertTrue(self.poll.is_poll())
