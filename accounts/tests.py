from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory

from . import models
from .views import profile
# Create your tests here.
from django.urls import reverse

from accounts.forms import ProfileForm
from accounts.models import Profile


class TestProfileModel(TestCase):
    def test_profile_creation(self):
        user = User.objects.create(
            username="testuserJ", password="testPassword")
        # Check that a Profile instance has been created
        self.assertIsInstance(user.profile, models.Profile)
        # Call the save method of the user to activate the signal
        # again, and check that it doesn't try to create another
        # profile instance
        user.save()
        self.assertIsInstance(user.profile, models.Profile)


class ProfileFormTest(TestCase):
    def test_saveProfileInput_whenValid_ShouldPassTest(self):
        data = {
            'username': 'Amelia',
            'first_name': 'Alelia',
            'last_name': 'Georgieva',
            'email': 'ameligeorgieva@abv.bg',

        }
        form = ProfileForm(data)
        self.assertTrue(form.is_valid())

    def test_Profile_WhenInvalidFirstName_ShouldPassTest(self):
        data = {
            'username': 'Amelia',
            'first_name': 'amelia',
            'last_name': 'Georgieva',
            'email': 'ameligeorgieva@abv.bg',

        }
        form = ProfileForm(data)
        self.assertFalse(form.is_valid())

    def test_Profile_WhenInvalidLastName_ShouldPassTest(self):
        data = {
            'username': 'Amelia',
            'first_name': 'Amelia',
            'last_name': 'georgieva',
            'email': 'ameligeorgieva@abv.bg',

        }
        form = ProfileForm(data)
        self.assertFalse(form.is_valid())


class ProfileViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='Jacob', password='top_secret1', email='jacob@gmail.com')

    def test_ViewUserProfile_WhenGetRequest_ShouldReturnUserProfile(self):
        request = self.factory.get('accounts/profile/')
        request.user = self.user
        response = profile(request)
        self.assertEqual(response.status_code, 200)

    def test_EditUserProfile_WhenGetRequest_ShouldReturnEditPage(self):
        request = self.factory.get('accounts/edit_profile/')
        request.user = self.user
        response = profile(request)
        self.assertEqual(response.status_code, 200)
