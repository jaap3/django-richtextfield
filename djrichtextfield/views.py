from django.views.generic import TemplateView
from djrichtextfield import settings


class InitView(TemplateView):
    template_name = 'djrichtextfield/init.js'
    content_type = 'application/javascript'

    def get_context_data(self, **kwargs):
        context_data = super(InitView, self).get_context_data(**kwargs)
        context_data['init_template'] = settings.CONFIG['init_template']
        return context_data

    def render_to_response(self, context, **response_kwargs):
        # Django 1.4 doesn't use self.content_type, so we fix this here
        return super(InitView, self).render_to_response(
            context, content_type=self.content_type, **response_kwargs)
