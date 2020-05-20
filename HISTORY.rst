History
-------

1.6 (2020-05-20)
^^^^^^^^^^^^^^^^^^

* init.js no longer depends on jQuery.
  This might a backwards incompatible change for:

  - Users that have defined their own init script that dependeds on
    the ``$e`` var. This var has been replaced by ``field`` which is
    a plain DOM node instead of a jQuery object.
  - Users that depended on the implicit load of Django's bundled
    version of jQuery now have explicitly load it themselves.

* Verified TinyMCE init/config works with TinyMCE 4 and 5

* Tested and verified to work with Django 3.1

1.5.0 (2019-12-04)
^^^^^^^^^^^^^^^^^^

* Drop support for Python 2
* Drop support for Django < 2.2
* Add support for Django 3.0


1.4.0 (2019-01-31)
^^^^^^^^^^^^^^^^^^

* NOTE: This is the final release that supports Python 2!
* Add support for plugable server side content sanitizers


1.3.0 (2018-11-05)
^^^^^^^^^^^^^^^^^^

* Allow CSS files to be included by a ``RichTextWidget``


1.2.4 (2018-09-25)
^^^^^^^^^^^^^^^^^^

* Fix display issue in Django 2.1's admin interface


1.2.3 (2018-09-11)
^^^^^^^^^^^^^^^^^^

* Add support for Django 2.1


1.2.2 (2018-06-12)
^^^^^^^^^^^^^^^^^^

* Conditionally load the (un)minified version of jquery depending on ``DEBUG``
* Load jQuery before all other scripts


1.2.1 (2018-01-18)
^^^^^^^^^^^^^^^^^^

* Add ``['admin/js/vendor/jquery/jquery.min.js', 'admin/js/jquery.init.js']``
  to ``RichTextWidget.media.js``. This makes the widget usable outside of the
  admin (but still requires ``django.contrib.admin`` to be in ``INSTALLED_APPS``)
  and prevents javascript errors inside the admin in certain edge cases.


1.2 (2017-12-04)
^^^^^^^^^^^^^^^^

* Remove support for Django < 1.11
* Add support for Django 2.0


1.1 (2016-01-14)
^^^^^^^^^^^^^^^^

* Remove support for Django < 1.8
* Tested with Django 1.8 & Django 1.9

1.0.1 (2014-11-13)
^^^^^^^^^^^^^^^^^^

* Fix unicode error

1.0 (2014-09-30)
^^^^^^^^^^^^^^^^

* First release
