======================
Django Rich Text Field
======================

A Django form and model field that renders a customizable rich text widget.
Tested with the WYSIWYG editors TinyMCE_ and CKEditor_ but can be easily
extended to use others.

Quickstart
----------

Install ``django-richtextfield`` and add it to your Django
project's ``INSTALLED_APPS``::

    INSTALLED_APPS += 'djrichtextfield'

Configure ``djrichtextfield`` (using TinyMCE from a CDN)::

    DJRICHTEXTFIELD_CONF = {
        'js': ['//tinymce.cachefly.net/4.1/tinymce.min.js'],
        'init_template': 'djrichtextfield/init/tinymce.js',
        'settings': {
            'menubar': False,
            'plugins': 'link image',
            'toolbar': 'bold italic | link image | removeformat',
            'width': 700
        }
    }

Now you're ready to use the field in your models and forms::

    from django.db import models
    from djrichtextfield.models import RichTextField

    class Post(models.Model):
        title = models.CharField(max_length=50)
        content = RichTextField()

or::

    from django import forms
    from djrichtextfield.widgets import RichTextWidget

    class CommentForm(forms.ModelForm):
        content = forms.CharField(widget=RichTextWidget())
        content.widget.field_settings = {'toolbar': 'bold italic'}

.. _TinyMCE: http://www.tinymce.com/
.. _CKEditor: http://ckeditor.com/
