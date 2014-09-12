import json
from django.test import TestCase
from django.test.utils import override_settings
from django.utils.html import escape
from testproject import settings
from djwysiwygfield.widgets import WysiwygWidget


class TestWysiwygWidget(TestCase):
    def test_css_class(self):
        """
        Has the djwysiwyg css class set
        """
        self.assertEqual(WysiwygWidget().attrs['class'], 'djwysiwyg')

    def test_attrs(self):
        """
        Takes attrs into account
        """
        widget = WysiwygWidget({'cols': 10})
        self.assertEqual(widget.attrs['cols'], 10)

    def test_css_class_addition(self):
        """
        Adds djwysiwyg to given css class
        """
        widget = WysiwygWidget({'class': 'somethingelse'})
        self.assertEqual(widget.attrs['class'], 'somethingelse djwysiwyg')


CONFIG = {
    'js': ['foo.js'],
    'settings': {'foo': True, 'bar': [1, 2, 3]}
}


@override_settings(DJWYSIWYG_CONFIG=CONFIG)
class SettingsTestCase(TestCase):
    config = CONFIG

    def setUp(self):
        self.widget = WysiwygWidget()

    def test_media_js(self):
        """
        Test that the correct javascript files are included.
        """
        self.assertEqual(self.config['js'], self.widget.media._js)

    def test_render(self):
        """
        Test that the rendered textarea is surrounded with a div and includes
        the wysiwyg-settings data attribute.
        """
        widget = WysiwygWidget()
        config = json.dumps(self.config['settings'])
        expected = ('<div class="field-box">'
                    '<textarea class="djwysiwyg" cols="40"'
                    ' data-wysiwyg-settings="{0}"'
                    ' name="" rows="10">\r\n</textarea>'
                    '</div>'.format(escape(config)))
        self.assertHTMLEqual(expected, widget.render('', ''))
