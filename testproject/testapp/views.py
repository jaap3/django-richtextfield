from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView, DetailView

from .forms import CommentForm
from .models import Comment, Post


class PostDetail(DetailView):
    model = Post


class CommentCreateView(UpdateView):
    model = Comment
    form_class = CommentForm

    def get_object(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return Comment(post=post)
