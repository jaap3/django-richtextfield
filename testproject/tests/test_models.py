from django.test import TestCase
from djwysiwygfield.models import WysiwygField
from djwysiwygfield.widgets import WysiwygWidget


class TestWysiwygField(TestCase):
    def test_formfield(self):
        self.assertIsInstance(WysiwygField().formfield().widget, WysiwygWidget)
