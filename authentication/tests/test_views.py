from django.test import TestCase
from faker import Faker
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import User

fake = Faker()


class TestCalls(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.password = fake.password()
        cls.username = fake.profile()["username"]
        cls.email = fake.email()
        cls.customer = User.objects.create_user(
            password=cls.password,
            full_name=fake.name(),
            email=cls.email,
        )

    def test_call_register(self):
        password = fake.password()
        data = {
            "password": password,
            "full_name": fake.name(),
            "email": fake.email(),
            "confirm_password": password,
        }

        response = self.client.post(
            "/api/v1/auth/register/", data, content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertIn("full_name", response.json())
        self.assertIn("email", response.json())

    def test_call_login(self):
        data = {"email": TestCalls.email, "password": TestCalls.password}

        response = self.client.post(
            "/api/v1/auth/login/", data, content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.json())
        self.assertIn("refresh", response.json())

    def test_call_refresh_token(self):
        refresh = RefreshToken.for_user(TestCalls.customer)
        data = {
            "refresh": str(refresh),
        }

        response = self.client.post(
            "/api/v1/auth/token/refresh/", data, content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.json())
