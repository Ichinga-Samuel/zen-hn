from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve


class TestAllAuthUrls(TestCase):
    username = "tes_tuser"
    email = "test_user@email.com"
    sign_up_url = reverse("account_signup")
    login_url = reverse("account_login")
    logout_url = reverse("account_logout")
    User = get_user_model()

    def setUp(self):
        ...

    def test_sign_up_url(self):
        res = self.client.get(self.sign_up_url)
        post = self.client.post(self.sign_up_url,
                         data={"email": self.email, "password1": "testpass123"})
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "account/signup.html")
        self.assertContains(res, "Sign Up")
        self.assertEqual(post.status_code, 302)
        new_user = self.User.objects.get(email=self.email)
        self.assertEqual(new_user.email, self.email)

    def test_login_url(self):
        res = self.client.get(self.login_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "account/login.html")
        self.assertContains(res, "Login")

    def test_logout(self):
        user = self.User.objects.create(email=self.email, username=self.username, password="testpass123")
        login = self.client.post(self.login_url, data={"email": user.email, "password": "testpass123"})
        self.assertEqual(login.status_code, 200)
        res = self.client.get(self.logout_url)
        self.assertEqual(res.status_code, 302)
