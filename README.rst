====================
Django WYSIWYG Field
====================

A Django form and model field that renders a customizable WYSIWYG widget.
Tested with TinyMCE_ CKEditor_ and Redactor_ but can be easily extended to use other editors.

Quickstart
----------

Install ``django-wysiwygfield`` and add it to your Django project's ``INSTALLED_APPS``::

    INSTALLED_APPS += 'djwysiwygfield'

Acquire a distribution of TinyMCE_, CKEditor_, Redactor_ or any other WYSIWYG editor and put the files in your project's ``STATIC_ROOT``.

Configure ``djwysiwygfield``::

    TODO: write configuration docs

Now you're ready to use the field in your models and forms::

    TODO: write usage docs

.. _TinyMCE: http://www.tinymce.com/
.. _CKEditor: http://ckeditor.com/
.. _Redactor: http://redactorjs.com/
