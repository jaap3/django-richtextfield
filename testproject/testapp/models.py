from django.db import models
from djwysiwygfield.models import WysiwygField


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = WysiwygField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField()

    def __str__(self):
        return 'Comment on "%s"' % self.post.title
