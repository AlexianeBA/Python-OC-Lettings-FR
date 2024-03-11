from django.test import TestCase, RequestFactory, SimpleTestCase
from .models import Letting, Address
from django.urls import reverse, resolve
from .views import index, letting

# Create your tests here.


class LettingModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street="Main St",
            city="City",
            state="NY",
            zip_code=12345,
            country_iso_code="USA",
        )
        self.letting = Letting.objects.create(
            title="Test Letting", address=self.address
        )

    def test_letting_creation(self):
        self.assertEqual(self.letting.title, "Test Letting")
        self.assertEqual(self.letting.address.number, 123)


class LettingViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.address = Address.objects.create(
            number=123,
            street="Main St",
            city="City",
            state="NY",
            zip_code=12345,
            country_iso_code="USA",
        )
        self.letting = Letting.objects.create(
            title="Test Letting", address=self.address
        )

    def test_index_view(self):
        request = self.factory.get("/lettings/")
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_letting_view(self):
        request = self.factory.get(f"/{self.letting.id}/")
        response = letting(request, letting_id=self.letting.id)
        self.assertEqual(response.status_code, 200)


class LettingURLTest(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse("lettings:letting")
        self.assertEqual(resolve(url).func, index)

    def test_letting_url_resolves(self):
        url = reverse("lettings:letting", args=[1])
        self.assertEqual(resolve(url).func, letting)
