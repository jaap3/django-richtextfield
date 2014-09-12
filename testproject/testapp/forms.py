from django import forms
from djwysiwygfield.widgets import WysiwygWidget


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=WysiwygWidget())
