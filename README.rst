======================
Django Rich Text Field
======================

.. image:: https://badge.fury.io/py/django-richtextfield.svg
    :target: https://pypi.python.org/pypi/django-richtextfield/
    :alt: Latest Version

.. image:: https://travis-ci.org/jaap3/django-richtextfield.svg?branch=master
    :target: https://travis-ci.org/jaap3/django-richtextfield

.. image:: https://coveralls.io/repos/jaap3/django-richtextfield/badge.svg?branch=master
    :target: https://coveralls.io/r/jaap3/django-richtextfield?branch=master

A Django model field and widget that renders a customizable rich
text/WYSIWYG widget.

Works in Django's admin interface and "normal" forms.

Supports global `editor settings`_, reusable `editor profiles`_
and per `field & widget settings`_. There's built-in support for
pluggable server side `content sanitizers`_.

Tested with TinyMCE_ and CKEditor_. Designed to be easily extended to
use other editors.


Quickstart
----------

Install ``django-richtextfield`` and add it to your Django
project's ``INSTALLED_APPS``, ``django.contrib.admin`` must also be in ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        'django.contrib.admin',
        ...
        'djrichtextfield'
    ]

Add the urls to the project's urlpatterns::

    path('djrichtextfield/', include('djrichtextfield.urls'))

Configure ``django-richtextfield`` in ``settings.py``::

    DJRICHTEXTFIELD_CONFIG = {
        'js': ['//cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js'],
        'init_template': 'djrichtextfield/init/tinymce.js',
        'settings': {
            'menubar': False,
            'plugins': 'link image',
            'toolbar': 'bold italic | link image | removeformat',
            'width': 700
        }
    }

Now you're ready to use the field in your models::

    from djrichtextfield.models import RichTextField

    class Post(models.Model):
        content = RichTextField()

or forms::

    from djrichtextfield.widgets import RichTextWidget

    class CommentForm(forms.ModelForm):
        content = forms.CharField(widget=RichTextWidget())


When using the editor outside of the admin make sure to include
``form.media`` in the ``<head>`` of the template::

    <head>
      ...
      {{ form.media }}
      ...
    </head>

Configuration
-------------

Define the ``DJRICHTEXTFIELD_CONFIG`` dictionary in your project settings.
This dictionary can have the following keys:

.. _conf_js:

Javascript souce(s)
^^^^^^^^^^^^^^^^^^^

``'js'``
    A list of required javascript files. These can be URLs to a CDN or paths
    relative to your ``STATIC_URL`` e.g.::

      'js': ['//cdn.ckeditor.com/4.14.0/standard/ckeditor.js']

    or::

      'js': ['path/to/editor.js', 'path/to/plugin.js']

.. _conf_css:

CSS souce(s)
^^^^^^^^^^^^

``'css'``
    A dictionary of CSS files required.
    These can be URLs to a CDN or paths relative to your ``STATIC_URL`` e.g.::

      'css': {
          'all': [
              'https://cdn.example.com/css/editor.css'
          ]
      }

    or::

      'css': {'all': ['path/to/editor.css', 'path/to/plugin.css']}


.. _conf_init_template:

Editor init template
^^^^^^^^^^^^^^^^^^^^

``'init_template'``
    Path to the `init template`_ for your editor. Currently
    ``django-richtextfield`` ships with two templates, either::

        'init_template': 'djrichtextfield/init/tinymce.js'

    or::

        'init_template': 'djrichtextfield/init/ckeditor.js'

.. _conf_settings:

Editor settings
^^^^^^^^^^^^^^^

``'settings'``
    A Python dictionary with the **default** configuration data for your
    editor e.g.::

      'settings': {  # TinyMCE
          'menubar': False,
          'plugins': 'link image',
          'toolbar': 'bold italic | link image | removeformat',
          'width': 700
      }

    or::

      'settings': {  # CKEditor
          'toolbar': [
              {'items': ['Format', '-', 'Bold', 'Italic', '-',
                         'RemoveFormat']},
              {'items': ['Link', 'Unlink', 'Image', 'Table']},
              {'items': ['Source']}
          ],
          'format_tags': 'p;h1;h2;h3',
          'width': 700
      }

.. _conf_profiles:

Editor profiles
^^^^^^^^^^^^^^^

``'profiles'``
  This is an **optional** configuration key. Profiles are "named" custom
  settings used to configure specific type of fields. You can configure
  profiles like this::

    'profiles': {
        'basic': {
            'toolbar': 'bold italic | removeformat'
        },
        'advanced': {
            'plugins': 'link image table code',
            'toolbar': 'formatselect | bold italic | removeformat |'
                       ' link unlink image table | code'
        }
    }

  .. note:: A profile is treated the same way as directly defined
            `field & widget settings`_. This means that
            profile settings are merged with the defaults!

.. _conf_sanitizer:

Content sanitizers
^^^^^^^^^^^^^^^^^^

``'sanitizer'``
    This is an **optional** configuration key. A sanitizer can be used to
    process submitted values before it is returned by the widget. By default no
    processing is performed on submitted values. You can configure a sanitizer
    either by providing a function or an importable path to a function, like
    so::

      'sanitizer': lambda value: '<h1>Title</h1>' + value

    or::

      'sanitizer': 'bleach.clean'

.. _conf_sanitizer_profiles:

``'sanitizer_profiles'``
    This is an **optional** configuration key. It is possible to override
    the default or configured sanitizer for each of the configured `profiles`_.
    For example to set a custom sanitizer for the ``advanced`` profile::

      'sanitizer_profiles': {
          'advanced': lambda value: value + 'This text has been sanitized.'
      }


Field & Widget settings
-----------------------

You can override the default settings per field::

    class CommentForm(forms.ModelForm):
        content = forms.CharField(widget=RichTextWidget())
        content.widget.field_settings = {'your': 'custom', 'settings': True}

or::

    class Post(models.Model):
        content = RichTextField(
            field_settings={'your': 'custom', 'settings': True},
            sanitizer='bleach.linkify'
        )

It's recommended to use `profiles`_, they make it easier to switch configs
or even editors on a later date. You use a profile like this::

    class CommentForm(forms.ModelForm):
        content = forms.CharField(widget=RichTextWidget(field_settings='basic'))

or::

    class Post(models.Model):
        content = RichTextField(field_settings='advanced')

.. note:: Fields always inherit the default settings, customs settings and
          profiles are merged with the defaults!


Custom init / Using another editor
----------------------------------

It should be fairly easy to use this project with another editor.
All that's required is to configure ``DJRICHTEXTFIELD_CONFIG`` to load the
right Javascript/CSS files and to create a custom `init template`_.

For example, to use jQuery based Summernote_ (lite) editor::

    DJRICHTEXTFIELD_CONFIG = {
        'js': [
            '//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.js',
            '//cdnjs.cloudflare.com/ajax/libs/summernote/0.8.9/summernote-lite.js',
        ],
        'css': {
            'all': [
                '//cdnjs.cloudflare.com/ajax/libs/summernote/0.8.9/summernote-lite.css',
            ]
        },
        'init_template': 'path/to/init/summernote.js',
        'settings': {
            'followingToolbar': False,
            'minHeight': 250,
            'width': 700,
            'toolbar': [
                ['style', ['bold', 'italic', 'clear']],
            ],
        }
    }

Init template
^^^^^^^^^^^^^

The init template is a Django template (so it should be in the template and
not in the static directory). It contains a tiny bit of Javascript that's
called to initialize each editor. For example, the init template for Summernote
would like this::

    $('#' + id).summernote(settings)

The init template has the following Javascript variables available from the
outer scope:

``field``
  DOM node of the textarea to be replaced
``id``
  The ``id`` attribute of the textarea
``default_settings``
  ``DJRICHTEXTFIELD_CONFIG['settings']`` as a JS object
``custom_settings``
  The ``field_settings`` as a JS object
``settings``
    Merge of ``default_settings`` and ``custom_settings``


Handling uploads & other advanced features
------------------------------------------

``django-richtextfield`` built to be editor agnostic. This means that it's
up to you to handle file uploads, show content previews and support
other "advanced" features.


.. _Profiles: conf_profiles_
.. _TinyMCE: https://www.tinymce.com/
.. _CKEditor: https://ckeditor.com/
.. _Summernote: https://summernote.org/
