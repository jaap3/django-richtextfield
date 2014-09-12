from django.test import TestCase
from django.core.urlresolvers import reverse


class TestUrls(TestCase):
    def test_reverse(self):
        url = reverse('djwysiwygfield_init')
        self.assertEqual(url, '/djwysiwygfield/init.js')
