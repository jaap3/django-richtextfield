from __future__ import unicode_literals
import json
from django.core.urlresolvers import reverse
from django.forms.widgets import Textarea, Media
from django.utils import six
from django.utils.encoding import force_text
from djrichtextfield import settings
try:
    from django.utils.html import format_html
except ImportError:  # Django 1.4
    from django.utils.safestring import mark_safe

    def format_html(format_string, *args, **kwargs):
        return mark_safe(format_string.format(*args, **kwargs))


class RichTextWidget(Textarea):
    CSS_CLASS = 'djrichtextfield'
    INIT_URL = 'djrichtextfield_init'
    SETTINGS_ATTR = 'data-field-settings'
    CONTAINER_CLASS = 'field-box'
    PROFILE_KEY = 'profiles'

    def __init__(self, attrs=None, field_settings=None):
        defaults = {'class': self.CSS_CLASS}
        if attrs:
            if 'class' in attrs:
                attrs['class'] = ' '.join([attrs['class'], defaults['class']])
            defaults.update(attrs)
        self.field_settings = field_settings or {}
        super(RichTextWidget, self).__init__(defaults)

    @property
    def media(self):
        js = settings.CONFIG['js']
        js.append(reverse(self.INIT_URL))
        return Media(js=js)

    def get_field_settings(self):
        """
        Get the field settings, if the configured setting is a string try
        to get a 'profile' from the global config.
        """
        field_settings = None
        if self.field_settings:
            if isinstance(self.field_settings, six.string_types):
                profiles = settings.CONFIG.get(self.PROFILE_KEY, {})
                field_settings = profiles.get(self.field_settings)
            else:
                field_settings = self.field_settings
        return field_settings

    def render(self, name, value, attrs=None):
        attrs = attrs or {}
        field_settings = self.get_field_settings()
        if field_settings:
            attrs[self.SETTINGS_ATTR] = json.dumps(field_settings,
                                                   default=force_text)
        textarea = super(RichTextWidget, self).render(name, value, attrs=attrs)
        return format_html(
            '<div class="{0}">{1}</div>', self.CONTAINER_CLASS, textarea)
