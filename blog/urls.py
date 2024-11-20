from blog.views import PostDetailView, PostListView
from django.urls import path


urlpatterns = [
   path('', PostListView.as_view(), name='post_list'),
   path('posts/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
]