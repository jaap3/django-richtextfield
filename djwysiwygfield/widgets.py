from django.forms.widgets import Textarea


class WysiwygWidget(Textarea):
    def __init__(self, attrs=None, wysiwyg_conf=None):
        defaults = {'class': 'djwysiwyg'}
        if attrs:
            if 'class' in attrs:
                attrs['class'] = ' '.join([attrs['class'], defaults['class']])
            defaults.update(attrs)
        self.wysiwyg_conf = wysiwyg_conf
        super(WysiwygWidget, self).__init__(defaults)
