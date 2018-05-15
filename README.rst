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
text/WYSIWYG widget. Tested with TinyMCE_ and CKEditor_. Designed to be
easily extended to use other editors.


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
        'js': ['//tinymce.cachefly.net/4.1/tinymce.min.js'],
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


Configuration
-------------

Define the ``DJRICHTEXTFIELD_CONFIG`` dictionary in your project settings.
This dictionary can have the following keys:

.. _conf_js:

``'js'``
    A list of required javascript files. These can be URLs to a CDN or paths
    relative to your ``STATIC_URL`` e.g.::

    'js': ['//cdn.ckeditor.com/4.4.4/standard/ckeditor.js']

    or::

    'js': ['path/to/editor.js', 'path/to/plugin.js']

.. _conf_init_template:

``'init_template'``
    Path to the `init template`_ for your editor. Currently
    ``django-richtextfield`` ships with two templates, either::

    'init_template': 'djrichtextfield/init/tinymce.js' 

    or::

    'init_template': 'djrichtextfield/init/ckeditor.js'

.. _conf_settings:

``'settings'``
    A Python dictionary with the **default** configuration data for your
    editor e.g.::

      {  # TinyMCE
          'menubar': False, 
          'plugins': 'link image',
          'toolbar': 'bold italic | link image | removeformat',
          'width': 700
      }

    or::

      {  # CKEditor
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

Field & Widget settings
^^^^^^^^^^^^^^^^^^^^^^^

You can override the default settings per field::

    class CommentForm(forms.ModelForm):
        content = forms.CharField(widget=RichTextWidget())
        content.widget.field_settings = {'your': 'custom', 'settings': True}

or::

    class Post(models.Model):
        content = RichTextField(field_settings={'your': 'custom', 'settings': True})

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

This is uncharted territory, but in theory it's fairly easy. Just configure
``DJRICHTEXTFIELD_CONFIG`` to load the right Javascript files and create
an `init template`_.

::

    DJRICHTEXTFIELD_CONFIG = {
        'js': ['path/to/editor.js'],
        'init_template': 'path/to/init/template.js',
        'settings': {'some': 'configuration'}
    }

Init template
^^^^^^^^^^^^^

The init template is a Django template (so it should be in the template and
not in the static directory). It contains a tiny bit of Javascript that's
called to initialize each editor. For example, the init template for CKEditor
looks like this::

    if (!CKEDITOR.instances[id]) {
        CKEDITOR.replace(id, settings);
    }

The init template has the following Javascript variables available from the
outer scope:

``$e``
  jQuery wrapped textarea to be replaced
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
.. _TinyMCE: http://www.tinymce.com/
.. _CKEditor: http://ckeditor.com/
