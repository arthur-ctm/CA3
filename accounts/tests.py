from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from cars.urls import *


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_login_view(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

        # test with valid credentials
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('car_list'))

        # test with invalid credentials
        data = {
            'username': 'invaliduser',
            'password': 'invalidpassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_signup_view(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

        # test with valid form data
        data = {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('car_list'))
        user = authenticate(username='newuser', password='newpassword')
        self.assertIsNotNone(user)

        # test with invalid form data
        data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_change_password_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('change_password')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_change.html')

        # test with valid form data
        data = {
            'old_password': 'testpassword',
            'new_password1': 'newpassword',
            'new_password2': 'newpassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('profile'))

        # test with invalid form data
        data = {
            'old_password': 'invalidpassword',
            'new_password1': 'newpassword',
            'new_password2': 'newpassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_change.html')
