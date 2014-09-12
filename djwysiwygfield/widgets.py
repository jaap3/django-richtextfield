import json
from django.core.urlresolvers import reverse
from django.forms.widgets import Textarea, Media
from djwysiwygfield import settings
try:
    from django.utils.html import format_html
except ImportError:  # Django 1.4
    from django.utils.safestring import mark_safe

    def format_html(format_string, *args, **kwargs):
        return mark_safe(format_string.format(*args, **kwargs))


class WysiwygWidget(Textarea):
    def __init__(self, attrs=None, wysiwyg_settings=None):
        defaults = {'class': 'djwysiwyg'}
        if attrs:
            if 'class' in attrs:
                attrs['class'] = ' '.join([attrs['class'], defaults['class']])
            defaults.update(attrs)
        self.wysiwyg_settings = wysiwyg_settings or {}
        super(WysiwygWidget, self).__init__(defaults)

    @property
    def media(self):
        js = settings.CONFIG['js']
        js.append(reverse('djwysiwygfield_init'))
        return Media(js=js)

    def render(self, name, value, attrs=None):
        attrs = attrs or {}
        wysiwyg_settings = settings.CONFIG['settings'].copy()
        wysiwyg_settings.update(self.wysiwyg_settings)
        attrs['data-wysiwyg-settings'] = json.dumps(wysiwyg_settings)
        textarea = super(WysiwygWidget, self).render(name, value, attrs=attrs)
        return format_html('<div class="field-box">{0}</div>', textarea)
