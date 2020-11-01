"""Test for register features"""


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