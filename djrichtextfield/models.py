from django.db import models
from djrichtextfield.widgets import RichTextWidget


class RichTextField(models.TextField):
    _south_introspects = True

    def formfield(self, **kwargs):
        return super(RichTextField, self).formfield(widget=RichTextWidget)
