class LoginTest(BaseTest):
    
    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_success(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(self.login_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)

    def test_cantlogin_with_no_username(self):
        response = self.client.post(self.login_url, {'password': 'passwped', 'username': ''}, format='text/html')
        self.assertEqual(response.status_code, 200)

    def test_cantlogin_with_no_password(self):
        response = self.client.post(self.login_url, {'username': 'passwped', 'password': ''}, format='text/html')
        self.assertEqual(response.status_code, 200)

