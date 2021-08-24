from django.http import response
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class LoginTest(TestCase):

    def setUp(self):
        self.credentials = {"username": "testuser", "password": "49a8ec447a8d"}
        test_user = User.objects.create_user(**self.credentials)
        test_user.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse("Claims"))
        self.assertRedirects(
            response, f"{reverse('login')}?next={reverse('Claims')}")

    def test_logged_in_template(self):
        login = self.client.login(username="testuser", password="49a8ec447a8d")
        response = self.client.get(reverse("Claims"))

        self.assertEqual(str(response.context['user']), "testuser")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "claims/submit.html")
