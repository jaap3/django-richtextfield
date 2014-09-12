from django.views.generic import TemplateView
from djwysiwygfield import settings


class WysiwygInitView(TemplateView):
    template_name = 'djwysiwygfield/init.js'
    content_type = 'application/javascript'

    def get_context_data(self, **kwargs):
        kwargs.update({
            'init': settings.CONFIG['init']
        })
        return super(WysiwygInitView, self).get_context_data(**kwargs)
