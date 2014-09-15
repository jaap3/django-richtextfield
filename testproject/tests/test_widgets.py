import json
from django.test import TestCase
from django.test.utils import override_settings
from django.utils.html import escape
from djrichtextfield.widgets import RichTextWidget


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


CONFIG = {
    'js': ['foo.js'],
    'settings': {'foo': True, 'bar': [1, 2, 3]}
}


@override_settings(DJRICHTEXTFIELD_CONFIG=CONFIG)
class SettingsTestCase(TestCase):
    config = CONFIG

    def setUp(self):
        self.widget = RichTextWidget()

    def test_media_js(self):
        """
        Test that the correct javascript files are included.
        """
        self.assertEqual(self.config['js'], self.widget.media._js)

    def test_render(self):
        """
        Test that the rendered textarea is surrounded with a div
        and includes the correct data attribute.
        """
        widget = RichTextWidget()
        config = json.dumps(self.config['settings'])
        expected = ('<div class="field-box">'
                    '<textarea class="djrichtextfield" cols="40"'
                    ' data-field-settings="{0}"'
                    ' name="" rows="10">\r\n</textarea>'
                    '</div>'.format(escape(config)))
        self.assertHTMLEqual(expected, widget.render('', ''))
