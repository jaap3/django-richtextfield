from django.test import TestCase
from django.test.utils import override_settings

from djrichtextfield import settings
from djrichtextfield.sanitizer import noop, SanitizerMixin


class TestSanitizerMixin(TestCase):
    def test_get_sanitizer_returns_provided_sanitzer(self):
        """
        Provided sanitizer is returned
        """
        sanitizer = object()
        mixin = SanitizerMixin(sanitizer=sanitizer)
        self.assertEqual(sanitizer, mixin.get_sanitizer())

    def test_get_sanitizer_uses_profile_sanitizer(self):
        """
        Sanitizer from settings for the given profile
        """
        mixin = SanitizerMixin()
        mixin.field_settings = 'baz'
        self.assertEqual(
            settings.CONFIG['sanitizer_profiles']['baz'],
            mixin.get_sanitizer())

    def test_clean_uses_global_sanitizer_with_no_sanitizer_profiles(self):
        """
        Global sanitizer from settings is returned if none match the profile
        """
        mixin = SanitizerMixin()
        mixin.field_settings = 'sanitizer_profile_does_not_exist'
        self.assertEqual(settings.CONFIG['sanitizer'], mixin.get_sanitizer())

    def test_clean_uses_global_sanitizer(self):
        """
        Global sanitizer from settings is returned
        """
        mixin = SanitizerMixin()
        self.assertEqual(settings.CONFIG['sanitizer'], mixin.get_sanitizer())

    @override_settings(DJRICHTEXTFIELD_CONFIG={})
    def test_clean_uses_noop_sanitizer(self):
        """
        No configured sanitizers causes noop to be used
        """
        mixin = SanitizerMixin()
        self.assertEqual(noop, mixin.get_sanitizer())

    def test_import_string(self):
        """
        Passing a function path causes it to be imported
        """
        mixin = SanitizerMixin(sanitizer='django.utils.text.slugify')
        sanitizer = mixin.get_sanitizer()
        self.assertEqual('django.utils.text', sanitizer.__module__)
        self.assertEqual('slugify', sanitizer.__name__)


class TestNoop(TestCase):
    def test_object_in_is_out(self):
        value = object()
        self.assertEqual(value, noop(value))

    def test_str_in_is_out(self):
        self.assertEqual('foo', noop('foo'))
