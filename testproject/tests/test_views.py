from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse


@override_settings(DJRICHTEXTFIELD_CONFIG={
    'init_template': 'djrichtextfield/init/tinymce.js'
})
class TestInitView(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('djrichtextfield_init'))

    def test_template(self):
        self.assertEqual(
            self.response.template_name, ['djrichtextfield/init.js'])

    def test_content_type(self):
        self.assertEqual(
            self.response['content-type'], 'application/javascript')

    def test_init_template_in_context(self):
        self.assertEqual('djrichtextfield/init/tinymce.js',
                         self.response.context_data['init_template'])
