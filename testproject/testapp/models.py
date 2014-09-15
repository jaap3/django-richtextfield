from django.db import models
from djrichtextfield.models import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=50)
    lead = RichTextField(field_settings='mini')
    content = RichTextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField()

    def __str__(self):
        return 'Comment on "%s"' % self.post.title
