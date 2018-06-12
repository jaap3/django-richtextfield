History
-------

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
