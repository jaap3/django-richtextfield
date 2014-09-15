from django import forms
from django.conf import settings
from djrichtextfield.widgets import RichTextWidget


CONF = settings.DJRICHTEXTFIELD_CONFIG

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=RichTextWidget())
    content.widget.field_settings = CONF.get('profiles', {}).get('mini')
