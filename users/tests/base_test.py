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
        }
        return super().setUp()
