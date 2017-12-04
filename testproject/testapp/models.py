from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from djrichtextfield.models import RichTextField


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=50)
    lead = RichTextField(field_settings='mini')
    content = RichTextField()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return 'Comment on "%s"' % self.post.title
