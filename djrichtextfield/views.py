from django.views.generic import TemplateView
from djrichtextfield import settings


class InitView(TemplateView):
    template_name = 'djrichtextfield/init.js'
    content_type = 'application/javascript'

    def get_context_data(self, **kwargs):
        kwargs.update({
            'init': settings.CONFIG['init']
        })
        return super(InitView, self).get_context_data(**kwargs)

    def render_to_response(self, context, **response_kwargs):
        # Django 1.4 doesn't use self.content_type, so we fix this here
        return super(InitView, self).render_to_response(
            context, content_type=self.content_type, **response_kwargs)
