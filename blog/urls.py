from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', cache_page(60)(BlogListView.as_view()), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='blog_view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]
