from django import forms

from djrichtextfield.widgets import RichTextWidget


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=RichTextWidget(field_settings='mini'))
