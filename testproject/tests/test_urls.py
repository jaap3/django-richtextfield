from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):
    def test_reverse(self):
        url = reverse('djrichtextfield_init')
        self.assertEqual(url, '/djrichtextfield/init.js')
