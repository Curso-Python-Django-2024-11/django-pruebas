from blog.views import PostListView
from django.urls import path


urlpatterns = [
   path('', PostListView.as_view(), name='post_list'),
]