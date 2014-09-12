from django.core.urlresolvers import reverse
from django.test import TestCase


class TestWysiwygInitView(TestCase):
    def test_template(self):
        response = self.client.get(reverse('djwysiwygfield_init'))
        self.assertEqual(response.template_name, ['djwysiwygfield/init.js'])

    def test_content_type(self):
        response = self.client.get(reverse('djwysiwygfield_init'))
        self.assertEqual(response['content-type'], 'application/javascript')
