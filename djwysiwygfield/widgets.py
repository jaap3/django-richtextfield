from django.core.urlresolvers import reverse
from django.forms.widgets import Textarea, Media
from django.utils.html import format_html
from djwysiwygfield import settings


class WysiwygWidget(Textarea):
    def __init__(self, attrs=None, wysiwyg_conf=None):
        defaults = {'class': 'djwysiwyg'}
        if attrs:
            if 'class' in attrs:
                attrs['class'] = ' '.join([attrs['class'], defaults['class']])
            defaults.update(attrs)
        self.wysiwyg_conf = wysiwyg_conf
        super(WysiwygWidget, self).__init__(defaults)

    @property
    def media(self):
        js = settings.CONFIG['js']
        js.append(reverse('djwysiwygfield_init'))
        return Media(js=js)

    def render(self, name, value, attrs=None):
        textarea = super(WysiwygWidget, self).render(name, value, attrs=attrs)
        return format_html('<div class="field-box">{0}</div>', textarea)
