from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse

from accounts.forms import ProfileForm
from accounts.models import Profile


class ProfileFormTest(TestCase):
    def test_saveProfileInput_whenValid_ShouldSaveProfile(self):
        data = {
            'username': 'Alelia',
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
        self.test_client = Client()

    def test_getProfile_whenProfile_ShouldRenderProfile(self):
        profile = Profile(username='testprofile', first_name='Anelia', last_name='Ivanova', email='anelia@yahoo.com')
        #don`t have user
        profile.save()
        response = self.test_client.get(reverse('user-profile'))
        self.assertTemplateUsed(response,'accounts/user_profile.html')
