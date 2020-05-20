from django import forms

from djrichtextfield.widgets import RichTextWidget

from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=RichTextWidget(field_settings='mini'))

    class Meta:
        model = Comment
        exclude = ['post']
