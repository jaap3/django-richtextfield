from django.test import TestCase, override_settings
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

    def test_render(self):
        """
        Test that the rendered textarea is surrounded with a clearing div
        """
        widget = WysiwygWidget()
        self.assertEqual(
            '<div class="field-box">'
            '<textarea class="djwysiwyg" cols="40" name="test" rows="10">\r\n'
            '</textarea></div>', widget.render('test', ''))


class SettingsTestCase(TestCase):
    settings = None

    def setUp(self):
        self.widget = WysiwygWidget()

    def test_media_js(self):
        self.assertEqual(self.settings['js'], self.widget.media._js)


@override_settings(DJWYSIWYG_CONFIG=settings.DJWYSIWYG_TINYMCE_CONFIG)
class TestTinyMCEWidget(SettingsTestCase):
    settings = settings.DJWYSIWYG_TINYMCE_CONFIG


@override_settings(DJWYSIWYG_CONFIG=settings.DJWYSIWYG_CKEDITOR_CONFIG)
class TestCKEditorWidget(SettingsTestCase):
    settings = settings.DJWYSIWYG_CKEDITOR_CONFIG


del SettingsTestCase
