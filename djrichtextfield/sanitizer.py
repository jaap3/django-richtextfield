from __future__ import unicode_literals

from django.utils import six
from django.utils.module_loading import import_string

from djrichtextfield import settings


def noop(value):
    return value


class SanitizerMixin(object):
    """
    Get the field sanitizer from the provided kwargs during init,
    or from the settings.
    """

    SANITIZER_KEY = 'sanitizer'
    SANITIZER_PROFILES_KEY = 'sanitizer_profiles'

    def __init__(self, *args, sanitizer=None, **kwargs):
        self.sanitizer = sanitizer
        super(SanitizerMixin, self).__init__(*args, **kwargs)

    def get_sanitizer(self):
        """
        Get the field sanitizer.

        The priority is the first defined in the following order:
        - A sanitizer provided to the widget.
        - Profile (field settings) specific sanitizer, if defined in settings.
        - Global sanitizer defined in settings.
        - Simple no-op sanitizer which just returns the provided value.

        """
        sanitizer = None
        if self.sanitizer:
            sanitizer = self.sanitizer
        elif (hasattr(self, 'field_settings')
              and isinstance(self.field_settings, six.string_types)):
            profiles = settings.CONFIG.get(self.SANITIZER_PROFILES_KEY, {})
            sanitizer = profiles.get(self.field_settings)

        if not sanitizer:
            sanitizer = settings.CONFIG.get(self.SANITIZER_KEY, noop)

        if isinstance(sanitizer, six.string_types):
            sanitizer = import_string(sanitizer)

        return sanitizer
