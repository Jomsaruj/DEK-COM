from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import SubComment


class QuestionTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("mo")
        self.user.save()
        self.sub_comment = SubComment.objects.create(author=self.user, comment_id_code ='123456', content='')

    def test_set_text(self):
        self.assertEqual('', self.sub_comment.content)
        self.sub_comment.set_text('real')
        self.assertEqual('real', self.sub_comment.content)