from django.core.urlresolvers import reverse
from django.test import TestCase


class TestUrls(TestCase):
    def test_reverse(self):
        url = reverse('djrichtextfield_init')
        self.assertEqual(url, '/djrichtextfield/init.js')
