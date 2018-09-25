import django
import json

from django.test import TestCase
from django.test.utils import override_settings
from django.utils.html import escape

from djrichtextfield.widgets import RichTextWidget

CONFIG = {
    'js': ['foo.js'],
    'settings': {'foo': True, 'bar': [1, 2, 3]},
    'profiles': {
        'simple': {'bar': [1, 2]}
    }
}


class TestRichTextWidget(TestCase):
    def test_css_class(self):
        """
        Has the correct css class set
        """
        self.assertEqual(RichTextWidget().attrs['class'], 'djrichtextfield')

    def test_attrs(self):
        """
        Takes attrs into account
        """
        widget = RichTextWidget({'cols': 10})
        self.assertEqual(widget.attrs['cols'], 10)

    def test_css_class_addition(self):
        """
        Adds to the given css class
        """
        widget = RichTextWidget({'class': 'somethingelse'})
        self.assertEqual(
            widget.attrs['class'], 'somethingelse djrichtextfield')


@override_settings(DJRICHTEXTFIELD_CONFIG=CONFIG)
class SettingsTestCase(TestCase):
    config = CONFIG
    container_class = RichTextWidget.CONTAINER_CLASS

    def setUp(self):
        self.widget = RichTextWidget()

    def test_media_js(self):
        """
        Test that the correct javascript files are included.
        """
        self.assertTrue(set(self.config['js']).issubset(self.widget.media._js))

    def test_render(self):
        """
        Test that the rendered textarea is surrounded with a div
        and doesn't include any settings.
        """
        widget = RichTextWidget()
        expected = ('<div class="{0}">'
                    '<textarea class="djrichtextfield" cols="40"'
                    ' name="" rows="10">\r\n</textarea>'
                    '</div>'.format(self.container_class))
        self.assertHTMLEqual(expected, widget.render('', ''))

    def test_render_with_settings(self):
        """
        The field includes the correct data attribute.
        """
        settings = {'foo': False}
        widget = RichTextWidget(field_settings=settings)
        config = json.dumps(settings)
        expected = ('<div class="{0}">'
                    '<textarea class="djrichtextfield" cols="40"'
                    ' data-field-settings="{1}"'
                    ' name="" rows="10">\r\n</textarea>'
                    '</div>'.format(self.container_class, escape(config)))
        self.assertHTMLEqual(expected, widget.render('', ''))

    def test_render_with_profile(self):
        """
        The field includes the correct data attribute.
        """
        widget = RichTextWidget(field_settings='simple')
        config = json.dumps(self.config['profiles']['simple'])
        expected = ('<div class="{0}">'
                    '<textarea class="djrichtextfield" cols="40"'
                    ' data-field-settings="{1}"'
                    ' name="" rows="10">\r\n</textarea>'
                    '</div>'.format(self.container_class, escape(config)))
        self.assertHTMLEqual(expected, widget.render('', ''))

    def test_render_with_missing_profile(self):
        """
        The field gets rendered without a data attribute.
        """
        widget = RichTextWidget(field_settings='missing')
        expected = ('<div class="{0}">'
                    '<textarea class="djrichtextfield" cols="40"'
                    ' name="" rows="10">\r\n</textarea>'
                    '</div>'.format(self.container_class))
        self.assertHTMLEqual(expected, widget.render('', ''))
