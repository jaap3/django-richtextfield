from django.db import models
from django.urls import reverse

from djrichtextfield.models import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=50)
    lead = RichTextField(field_settings='mini')
    content = RichTextField()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def get_add_comment_url(self):
        return reverse('post_add_comment', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    def get_absolute_url(self):
        return '{}#c{}'.format(reverse('post_detail', kwargs={'pk': self.post.pk}), self.pk)

    def __str__(self):
        return 'Comment on "%s"' % self.post.title
