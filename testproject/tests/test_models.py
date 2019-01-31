from django.core.exceptions import ValidationError
from django.test import TestCase

from djrichtextfield.models import RichTextField
from djrichtextfield.widgets import RichTextWidget


def empty_string(value):
    return ''


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

    def test_formfield_widget_passes_sanitizer(self):
        """
        Model field passes sanitizer to widget
        """
        sanitizer = object()
        widget = RichTextField(sanitizer=sanitizer).formfield().widget
        self.assertEqual(widget.sanitizer, sanitizer)

    def test_clean_uses_sanitizer(self):
        """
        Model field sanitizes values on clean with the provided sanitizer
        """
        field = RichTextField(sanitizer=lambda value: 'test' + value)
        self.assertEqual('testbar', field.clean('bar', None))

    def test_field_validates_after_sanitizer(self):
        """
        Required field raises ValidationError if sanitizer returns empty
        """
        field = RichTextField(blank=False, sanitizer=empty_string)
        self.assertRaises(ValidationError, field.clean, 'fancy text', None)

        # No error if field is allowed to be blank
        field = RichTextField(blank=True, sanitizer=empty_string)
        field.clean('fancy text', None)

    def test_sanitizer_handles_none(self):
        """
        value_from_datadict doesn't sanitize None values
        """
        field = RichTextField(blank=True, null=True)
        try:
            field.clean(None, None)
        except Exception:
            raise AssertionError('Expected no errors')
