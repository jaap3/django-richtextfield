from __future__ import unicode_literals

from django.conf.urls import url

from djrichtextfield.views import InitView

urlpatterns = [
    url('^init.js$', InitView.as_view(), name='djrichtextfield_init')
]
