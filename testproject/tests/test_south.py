from django.test import TestCase
from django.utils.unittest import skipUnless
from djwysiwygfield.models import WysiwygField
try:
    from south import modelsinspector
except ImportError:
    modelsinspector = False


@skipUnless(modelsinspector, 'South is not installed')
class TestSouthIntrospection(TestCase):
    def test_field_can_introspect(self):
        self.assertTrue(modelsinspector.can_introspect(WysiwygField))
