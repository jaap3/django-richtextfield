from django.test import TestCase
from django.utils.unittest import skipUnless
from djrichtextfield.models import RichTextField
from djrichtextfield.widgets import RichTextWidget
try:
    from south import modelsinspector
except ImportError:
    modelsinspector = False


class TestRichTextField(TestCase):
    def test_formfield_widget(self):
        """
        Formfield has RichTextWidget
        """
        self.assertIsInstance(
            RichTextField().formfield().widget, RichTextWidget)

    @skipUnless(modelsinspector, 'South is not installed')
    def test_field_can_introspect(self):
        """
        South can introspect this field
        """
        self.assertTrue(modelsinspector.can_introspect(RichTextField))
