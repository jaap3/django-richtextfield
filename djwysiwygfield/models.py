from django.db import models
from djwysiwygfield.widgets import WysiwygWidget


class WysiwygField(models.TextField):
    _south_introspects = True

    def formfield(self, **kwargs):
        return super(WysiwygField, self).formfield(widget=WysiwygWidget)
