from __future__ import unicode_literals

from django.db import models

from djrichtextfield.sanitizer import SanitizerMixin
from djrichtextfield.widgets import RichTextWidget


class RichTextField(SanitizerMixin, models.TextField):
    def __init__(self, *args, **kwargs):
        # Python 2 does not allow keywords between *args and **kwargs
        self.field_settings = kwargs.pop('field_settings', None)
        super(RichTextField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = RichTextWidget(
            field_settings=self.field_settings, sanitizer=self.sanitizer)
        return super(RichTextField, self).formfield(**kwargs)

    def clean(self, value, model_instance):
        """
        Convert the value's type, sanitize it, and run validation. Validation
        errors from to_python() and validate() are propagated. Return the
        correct value if no error is raised.
        """
        value = self.to_python(value)
        if value is not None:
            value = self.get_sanitizer()(value)
        self.validate(value, model_instance)
        self.run_validators(value)
        return value
