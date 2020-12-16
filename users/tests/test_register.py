"""Test for register features"""

"""The setUp for all tests in users."""
from django.test import TestCase
from django.urls import reverse


class BaseTest(TestCase):
    """Base information for test in users."""

    def setUp(self):
        """Initial set up with username and password."""
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user = {
            'username': 'username',
            'password': 'password',
        }
        self.user_short_password = {
            'username': 'username',
            'password': 'tes',
        }
        self.user_unmatching_password = {
            'username': 'username',
            'password': 'teslatt',
        }

        self.user_invalid_email = {
            'username': 'username',
            'password': 'teslatt',
            'email': 'asdfghjk'        
            }
        return super().setUp()

class RegisterTest(BaseTest):
    """Test with many situation when user register."""

    def test_can_view_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_can_register_user(self):
        response = self.client.post(self.register_url, self.user,
                                    format='text/html')
        self.assertEqual(response.status_code, 200)

    def test_cant_register_user_with_unmatching_passwords(self):
        response = self.client.post(self.register_url,
                                    self.user_unmatching_password, format ='text/html')
        self.assertEqual(response.status_code, 200)

    def test_cant_register_user_with_invalid_email(self):
        response = self.client.post(self.register_url,
                                    self.user_invalid_email, format ='text/html')
        self.assertEqual(response.status_code, 200)