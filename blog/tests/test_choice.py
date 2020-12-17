from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Choice


class ChoiceTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("mo")
        self.user.save()
        self.choice = Choice.objects.create(id_code='123456')

    def test_get_vote_percent(self):
        self.assertEqual(0,self.choice.get_vote_percent())
        self.choice2 = Choice.objects.create(id_code='123456', votes=5, all_votes=10)
        self.assertEqual(50.0,self.choice2.get_vote_percent())
