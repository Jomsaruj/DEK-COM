from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Job

class JobTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("mo")
        self.user.save()
        self.job = Job.objects.create(author=self.user, topic='test', id_code='123456', content='')

    def test_has_content(self):
        self.assertFalse(self.job.has_content())
        self.job2 = Job.objects.create(author=self.user, topic='test2', id_code='555555', content='want')
        self.assertTrue(self.job2.has_content())

    def test_has_link(self):
        self.assertFalse(self.job.has_link())
        self.job2 = Job.objects.create(author=self.user, topic='test2', id_code='555555', content='', link='youtube')
        self.assertTrue(self.job2.has_link())
