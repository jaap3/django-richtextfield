import json
from django.core.urlresolvers import reverse
from django.forms.widgets import Textarea, Media
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

    def render(self, name, value, attrs=None):
        attrs = attrs or {}
        field_settings = settings.CONFIG['settings'].copy()
        field_settings.update(self.field_settings)
        attrs[self.SETTINGS_ATTR] = json.dumps(field_settings)
        textarea = super(RichTextWidget, self).render(name, value, attrs=attrs)
        return format_html(
            '<div class="{0}">{1}</div>', self.CONTAINER_CLASS, textarea)
