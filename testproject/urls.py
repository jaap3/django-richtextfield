from django.urls import include, path
from django.contrib import admin

from .testapp.views import CommentCreateView, PostDetail


admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='post_add_comment')
]
