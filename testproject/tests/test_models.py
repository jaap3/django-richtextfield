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
        Model field has RichTextWidget
        """
        self.assertIsInstance(
            RichTextField().formfield().widget, RichTextWidget)

    def test_formfield_widget_passes_settings(self):
        """
        Model field passes setting to widget
        """
        settings = {'foo': True, 'bar': [1, 2, 3]}
        widget = RichTextField(field_settings=settings).formfield().widget
        self.assertEqual(widget.field_settings, settings)

    @skipUnless(modelsinspector, 'South is not installed')
    def test_field_can_introspect(self):
        """
        South can introspect this field
        """
        self.assertTrue(modelsinspector.can_introspect(RichTextField))
