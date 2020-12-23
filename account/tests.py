from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserManagersTests(TestCase):

    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(email='normal@user.com', password='foo', username='normal')
        self.admin_user = self.User.objects.create_superuser('super@user.com', 'super', 'foo')

    def test_create_user(self):
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertEqual(self.user.username, 'normal')
        self.assertEqual(self.user.USERNAME_FIELD, 'email')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
        with self.assertRaises(TypeError):
            self.User.objects.create_user()
        with self.assertRaises(TypeError):
            self.User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            self.User.objects.create_user(email='', password="foo", username='')

    def test_create_superuser(self):
        self.assertEqual(self.admin_user.email, 'super@user.com')
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_superuser)
        with self.assertRaises(ValueError):
            self.User.objects.create_superuser(
                email='',username='', password='foo')


class CustomUserTests(TestCase):

    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(email='normal@user.com', password='foo', username='normal')

    def test_usernameField_is_emailField (self):
        self.assertEqual(self.user.USERNAME_FIELD, 'email')

    def test_usernameField_is_the_user_email (self):
        self.assertEqual(self.user.email, 'normal@user.com')

    def test_usernameField_in_requiredFields(self):
        self.assertIn('username', self.user.REQUIRED_FIELDS)
