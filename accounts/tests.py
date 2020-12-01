from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from .views import profile
# Create your tests here.
from django.urls import reverse

from accounts.forms import ProfileForm
from accounts.models import Profile


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

    def test_Userprofile_WhenGetRequest_ShouldReturnUserProfile(self):
        request = self.factory.get('accounts/profile/')
        request.user = self.user
        response = profile(request)
        self.assertEqual(response.status_code, 200)

    def test_AnonymousUser_whenAddNews_ShouldReturnLoginNext(self):
        response = self.client.get('/create_article/', follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/create_article/')
