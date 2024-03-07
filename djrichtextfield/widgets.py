import json

from django.forms.widgets import Media, Textarea
from django.urls import reverse
from django.utils.encoding import force_str
from django.utils.html import format_html

from djrichtextfield import settings
from djrichtextfield.sanitizer import SanitizerMixin


class RichTextWidget(SanitizerMixin, Textarea):
    CSS_CLASS = "djrichtextfield"
    INIT_URL = "djrichtextfield_init"
    SETTINGS_ATTR = "data-field-settings"
    CONTAINER_CLASS = "fieldBox"
    PROFILE_KEY = "profiles"

    def __init__(self, attrs=None, field_settings=None, sanitizer=None):
        defaults = {"class": self.CSS_CLASS}
        if attrs:
            if "class" in attrs:
                attrs["class"] = " ".join(
                    [
                        attrs["class"],
                        defaults["class"],
                    ]
                )
            defaults.update(attrs)
        self.field_settings = field_settings or {}
        super(RichTextWidget, self).__init__(defaults, sanitizer=sanitizer)

    @property
    def media(self):
        js = []
        js.extend(settings.CONFIG["js"])
        js.append(reverse(self.INIT_URL))
        return Media(js=js, css=settings.CONFIG["css"])

    def get_field_settings(self):
        """
        Get the field settings, if the configured setting is a string
        try to get a 'profile' from the global config.
        """
        field_settings = None
        if self.field_settings:
            if isinstance(self.field_settings, str):
                profiles = settings.CONFIG.get(self.PROFILE_KEY, {})
                field_settings = profiles.get(self.field_settings)
            else:
                field_settings = self.field_settings
        return field_settings

    def render(self, name, value, attrs=None, renderer=None):
        attrs = attrs or {}
        field_settings = self.get_field_settings()
        if field_settings:
            attrs[self.SETTINGS_ATTR] = json.dumps(field_settings, default=force_str)
        textarea = super(RichTextWidget, self).render(
            name, value, attrs=attrs, renderer=renderer
        )
        return format_html('<div class="{0}">{1}</div>', self.CONTAINER_CLASS, textarea)

    def value_from_datadict(self, *args, **kwargs):
        """
        Pass the submitted value through the sanitizer before returning it.
        """
        value = super(RichTextWidget, self).value_from_datadict(*args, **kwargs)
        if value is not None:
            value = self.get_sanitizer()(value)
        return value
