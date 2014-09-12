from django.conf.urls import url
from djwysiwygfield.views import WysiwygInitView

urlpatterns = [
    url('^init.js$', WysiwygInitView.as_view(), name='djwysiwygfield_init')
]
