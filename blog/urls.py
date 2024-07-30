from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView)

from . import views

urlpatterns = [
   path('', PostListView.as_view(),name='blog-home'),
   path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
   path('detail/<int:pk>', PostDetailView.as_view(), name='post-detail'),
   path('create/', PostCreateView.as_view(), name='post-create'),
   path('detail/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
   path('detail/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete')


]