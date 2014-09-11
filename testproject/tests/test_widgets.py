from django.test import TestCase
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
