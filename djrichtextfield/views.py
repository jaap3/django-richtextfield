from __future__ import unicode_literals

import json

from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView

from djrichtextfield import settings


class InitView(TemplateView):
    template_name = 'djrichtextfield/init.js'
    content_type = 'application/javascript'

    def get_settings_json(self):
        return mark_safe(json.dumps(settings.CONFIG['settings'],
                                    default=force_text))

    def get_context_data(self, **kwargs):
        context_data = super(InitView, self).get_context_data(**kwargs)
        context_data['default_settings'] = self.get_settings_json()
        context_data['init_template'] = settings.CONFIG['init_template']
        return context_data
