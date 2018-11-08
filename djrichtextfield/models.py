from __future__ import unicode_literals

from django.db import models

from djrichtextfield.widgets import RichTextWidget


class RichTextField(models.TextField):
    def __init__(self, *args, **kwargs):
        self.field_settings = kwargs.pop('field_settings', None)
        super(RichTextField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = RichTextWidget(field_settings=self.field_settings)
        return super(RichTextField, self).formfield(**kwargs)
