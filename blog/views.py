from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

# Create your views here.


# Lista de posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/postlist.html'


# Detalle de un post concreto
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/postdetail.html'