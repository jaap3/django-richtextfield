from django.urls import path

from djrichtextfield.views import InitView

urlpatterns = [
    path("init.js", InitView.as_view(), name="djrichtextfield_init"),
]
