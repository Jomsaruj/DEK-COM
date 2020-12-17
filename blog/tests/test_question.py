from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Question


class QuestionTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("mo")
        self.user.save()
        self.question = Question.objects.create(author=self.user, topic='test', id_code='123456', content='')

    def test_has_content(self):
        self.assertFalse(self.question.has_content())
        self.question2 = Question.objects.create(author=self.user, topic='test2', id_code='555555', content='want')
        self.assertTrue(self.question2.has_content())
