from django.test import TestCase, RequestFactory, SimpleTestCase
from django.urls import reverse, resolve
from .models import Profile
from .views import index, profile
from django.contrib.auth.models import User


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(self.profile.favorite_city, "Test City")


class ProfileViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_index_view(self):
        request = self.factory.get("/")
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_profile_view(self):
        request = self.factory.get("/testuser/")
        response = profile(request, username="testuser")
        self.assertEqual(response.status_code, 200)


class ProfileURLTest(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse("profiles:profiles")
        self.assertEqual(resolve(url).func, index)

    def test_letting_url_resolves(self):
        url = reverse("profiles:profiles", args=[1])
        self.assertEqual(resolve(url).func, profile)


class IntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(self.profile.favorite_city, "Test City")

    def test_index_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_profile_view(self):
        response = self.client.get("/profiles/", args=[self.profile.favorite_city])
        self.assertEqual(response.status_code, 200)

    def test_profile_url(self):
        response = self.client.get(reverse("profiles:profiles"))
        self.assertEqual(response.status_code, 200)
