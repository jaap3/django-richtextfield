from django.test import TestCase

from djrichtextfield.models import RichTextField
from djrichtextfield.widgets import RichTextWidget


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
