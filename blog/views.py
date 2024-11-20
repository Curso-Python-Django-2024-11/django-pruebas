from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

# Create your views here.


# Lista de posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/postlist.html'

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by("-created_at")


# Detalle de un post concreto
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/postdetail.html'