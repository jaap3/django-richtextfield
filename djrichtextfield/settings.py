from __future__ import unicode_literals

from django.conf import settings
from django.dispatch import receiver
from django.test.signals import setting_changed

DEFAULT_CONFIG = {
    'js': [],
    'init_template': None,
    'settings': {}
}
CONFIG = DEFAULT_CONFIG.copy()
CONFIG.update(getattr(settings, 'DJRICHTEXTFIELD_CONFIG', {}))


@receiver(setting_changed)
def update_settings(setting=None, value=None, **kwargs):
    global CONFIG
    if setting == 'DJRICHTEXTFIELD_CONFIG':  # pragma: no branch
        CONFIG = DEFAULT_CONFIG.copy()
        if value:  # pragma: no branch
            CONFIG.update(value)
