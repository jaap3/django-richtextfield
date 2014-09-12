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

    def render_to_response(self, context, **response_kwargs):
        # Django 1.4 doesn't use self.content_type, so we fix this here
        return super(WysiwygInitView, self).render_to_response(
            context, content_type=self.content_type, **response_kwargs)
