from django.test import TestCase, RequestFactory, SimpleTestCase
from django.urls import reverse, resolve
from .models import Profile
from .views import index, profile
from django.contrib.auth.models import User


class ProfileModelTest(TestCase):
    """
    Test case for the Profile model.
    """

    def setUp(self):
        """
        Set up the test environment by creating a user and a profile.
        """
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_profile_creation(self):
        """
        Test case for profile creation.

        This method tests the creation of a profile and verifies that the user's username
        and favorite city are set correctly.

        Assertions:
        - The user's username should be "testuser".
        - The favorite city should be "Test City".
        """
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(self.profile.favorite_city, "Test City")


class ProfileViewsTest(TestCase):
    """
    Test case for testing profile views.
    """

    def setUp(self):
        """
        Set up the test environment before each test case is executed.

        This method is called before each test case is run. It initializes the necessary objects and data for the test case.
        In this case, it creates a RequestFactory object, a User object, and a Profile object associated with the user.
        """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_index_view(self):
        """
        Test case for the index view.

        This method tests the behavior of the index view by making a GET request to the root URL ("/")
        and asserting that the response status code is 200 (OK).

        """
        request = self.factory.get("/")
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_profile_view(self):
        """
        Test case for the profile view.

        This method tests the behavior of the profile view when a request is made
        to view a user's profile. It verifies that the response status code is 200,
        indicating a successful request.

        """
        request = self.factory.get("/testuser/")
        response = profile(request, username="testuser")
        self.assertEqual(response.status_code, 200)


class ProfileURLTest(SimpleTestCase):
    """
    Test case for testing URL resolution of profile-related views.
    """

    def test_index_url_resolves(self):
        """
        Test that the URL for the index view resolves correctly.
        """
        url = reverse("profiles:profiles")
        self.assertEqual(resolve(url).func, index)

    def test_letting_url_resolves(self):
        """
        Test case to verify that the URL for the 'profiles' view resolves correctly.
        """
        url = reverse("profiles:profiles", args=[1])
        self.assertEqual(resolve(url).func, profile)


class IntegrationTest(TestCase):
    """
    A test case for integration testing of the Profile app.
    """

    def setUp(self):
        """
        Set up the test environment by creating a user and a profile.
        """
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_profile_creation(self):
        """
        Test case to verify the creation of a profile.

        This test checks if the profile is created correctly by asserting the username and favorite city.

        """
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(self.profile.favorite_city, "Test City")

    def test_index_view(self):
        """
        Test case for the index view.

        This method sends a GET request to the root URL ("/") and asserts that the response
        status code is 200 (OK).

        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_profile_view(self):
        """
        Test case for the profile view.

        This method tests the behavior of the profile view when a GET request is made to the "/profiles/" URL
        with the profile's favorite city as an argument. It asserts that the response status code is 200,
        indicating a successful request.

        """
        response = self.client.get("/profiles/", args=[self.profile.favorite_city])
        self.assertEqual(response.status_code, 200)

    def test_profile_url(self):
        """
        Test the profile URL.

        This method sends a GET request to the profile URL and checks if the response status code is 200 (OK).

        """
        response = self.client.get(reverse("profiles:profiles"))
        self.assertEqual(response.status_code, 200)
