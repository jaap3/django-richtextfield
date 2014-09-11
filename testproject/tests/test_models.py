from django.test import TestCase
from django.utils.unittest import skipUnless
from djwysiwygfield.models import WysiwygField
from djwysiwygfield.widgets import WysiwygWidget
try:
    from south import modelsinspector
except ImportError:
    modelsinspector = False


class TestWysiwygField(TestCase):
    def test_formfield_widget(self):
        """
        Formfield has WysiwygWidget
        """
        self.assertIsInstance(WysiwygField().formfield().widget, WysiwygWidget)

    @skipUnless(modelsinspector, 'South is not installed')
    def test_field_can_introspect(self):
        """
        South can introspect this field
        """
        self.assertTrue(modelsinspector.can_introspect(WysiwygField))
