from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_homepage_returns_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'core/home.html')
