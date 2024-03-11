from django.test import TestCase
from django.urls import reverse


class TestHomePage(TestCase):
    def test_dummy(self):
        assert 1

    def test_home_page(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_admin_page(self):
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 302)

    def test_profile_page(self):
        response = self.client.get("/profiles/")
        self.assertEqual(response.status_code, 200)

    def test_lettings_page(self):
        response = self.client.get("/lettings/")
        self.assertEqual(response.status_code, 200)

    def test_404_page(self):
        response = self.client.get("/error/404/")
        self.assertEqual(response.status_code, 404)

    def test_500_page(self):
        response = self.client.get("/error/500/")
        self.assertEqual(response.status_code, 500)
