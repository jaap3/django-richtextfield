from django.core.urlresolvers import reverse
from django.test import TestCase


class TestInitView(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('djrichtextfield_init'))

    def test_template(self):
        self.assertEqual(
            self.response.template_name, ['djrichtextfield/init.js'])

    def test_content_type(self):
        self.assertEqual(
            self.response['content-type'], 'application/javascript')
