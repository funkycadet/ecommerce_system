from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

class AuthenticationTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'StrongPass123!',
            'password2': 'StrongPass123!'
        }
        self.signup_url = '/auth/signup'
        self.login_url = '/auth/login'

    def test_signup_success(self):
        data = self.user_data
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        # self.assertIn('tokens', response.data['user'])

    def test_signup_password_mismatch(self):
        data = self.user_data.copy()
        data['password2'] = 'DifferentPass123!'
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertIn('password', response.data)

    def test_signup_weak_password(self):
        data = self.user_data.copy()
        data['password'] = data['password2'] = '123'
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_duplicate_username(self):
        User.objects.create_user(username='testuser', password='StrongPass123!')
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_success(self):
        User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='StrongPass123!',
        )
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'StrongPass123!'
        }) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('tokens', response.data)
        # self.assertIn('refresh', response.data['tokens'])
        self.assertIn('access_token', response.data['tokens'])

    def test_login_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'nonexistent',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertIn('error', response.data)

    def test_login_missing_fields(self):
        response = self.client.post(self.login_url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)




# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth.models import User
# from rest_framework.test import APIClient
# from rest_framework import status

# class AuthenticationTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.signup_url = '/auth/signup'
#         self.login_url = '/auth/login'
#         self.user_data = {
#                 'username': 'testuser',
#                 'email': 'test@example.com',
#                 'password': 'StrongPass123!',
#                 'password2': 'StrongPass123!'
#             }
#         }
#         self.login_data = {
#             'data': {
#                 'username': 'testuser',
#                 'password': 'StrongPass123!'
#             }
#         }

#     def test_signup_success(self):
#         response = self.client.post(self.signup_url, self.user_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertTrue(User.objects.filter(username='testuser').exists())

#     def test_signup_password_mismatch(self):
#         data = self.user_data.copy()
#         data['data']['password2'] = 'DifferentPass123!'
#         response = self.client.post(self.signup_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_signup_weak_password(self):
#         data = self.user_data.copy()
#         data['data']['password'] = data['data']['password2'] = '123'
#         response = self.client.post(self.signup_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_signup_duplicate_username(self):
#         User.objects.create_user(username='testuser', password='StrongPass123!')
#         response = self.client.post(self.signup_url, self.user_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_login_success(self):
#         User.objects.create_user(
#             username='testuser',
#             email='test@example.com',
#             password='StrongPass123!'
#         )
#         response = self.client.post(self.login_url, self.login_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('tokens', response.data)

#     def test_login_invalid_credentials(self):
#         data = {'data': {'username': 'nonexistent', 'password': 'wrongpass'}}
#         response = self.client.post(self.login_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_login_missing_fields(self):
#         response = self.client.post(self.login_url, {}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
