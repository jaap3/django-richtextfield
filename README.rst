====================
Django WYSIWYG Field
====================

A Django form and model field that renders a customizable WYSIWYG widget.
Tested with TinyMCE_ and CKEditor_ but can be easily extended to use
other editors.

Quickstart
----------

Install ``django-wysiwygfield`` and add it to your Django
project's ``INSTALLED_APPS``::

    INSTALLED_APPS += 'djwysiwygfield'

Configure ``djwysiwygfield`` (using TinyMCE from a CDN)::

    DJWYSIWYG_CONF = {
        'js': ['//tinymce.cachefly.net/4.1/tinymce.min.js']
    }

Now you're ready to use the field in your models and forms::

    from django.db import models
    from djwysiwygfield.models import WysiwygField

    class Post(models.Model):
        title = models.CharField(max_length=50)
        content = WysiwygField()

or::

    from django import forms
    from djwysiwygfield.widgets import WysiwygWidget

    class CommentForm(forms.ModelForm):
        content = forms.CharField(widget=WysiwygWidget)

.. _TinyMCE: http://www.tinymce.com/
.. _CKEditor: http://ckeditor.com/
