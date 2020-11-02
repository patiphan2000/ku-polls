from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from ..models import Question

class AuthTest(TestCase):
    def test_login_with_not_exist_account(self):
        self.assertFalse(self.client.login(user='this_account@notExist', password='00000'))

    def test_login(self):
        user = User.objects.create(username='testuser')
        user.set_password('55555')
        user.save()

        self.assertTrue(self.client.login(username='testuser', password='55555'))

    def test_logout_with_no_user(self):
        self.assertFalse(self.client.logout())  # logout with no user should return false.

    def test_logout(self):
        user = User.objects.create(username='testuser')
        user.set_password('55555')
        user.save()

        self.client.login(username='testuser', password='55555')
        self.assertIsNone(self.client.logout())