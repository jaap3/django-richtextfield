from django.conf import settings
from django.dispatch import receiver
from django.test.signals import setting_changed

DEFAULT_CONFIG = {
    'js': [],
    'init': 'alert(id);',
    'settings': {}
}
CONFIG = DEFAULT_CONFIG.copy()
CONFIG.update(getattr(settings, 'DJWYSIWYG_CONFIG', {}))


@receiver(setting_changed)
def update_settings(setting=None, value=None, enter=None, **kwargs):
    global CONFIG
    if setting == 'DJWYSIWYG_CONFIG':
        CONFIG = DEFAULT_CONFIG.copy()
        if enter:
            CONFIG.update(value)
