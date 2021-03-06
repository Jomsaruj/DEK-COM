"""Test for create post."""
from django.test import TestCase
from django.urls import reverse


class BlogTest(TestCase):

    def setUp(self):
        self.home_page = reverse('blog:blog-index')
        self.login_url = reverse('login')
        self.user_1 = {
            'username': 'username1',
            'password': 'password',
        }
        self.user_2 = {
            'username': 'username2',
            'password': 'password',
        }        

    def test_access_home_page(self):    
        response = self.client.get(self.home_page)
        self.assertEqual(response.status_code, 200)

    def test_other_user_visit_post(self):
        self.client.post(self.login_url, self.user_1, format='text/html')
        self.client.logout()
        url = reverse('blog:blog-index')
        response = self.client.get(url)
        self.assertContains(response, "All blog")

         
