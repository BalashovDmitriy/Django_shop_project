from django.urls import path

from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, toggle_active

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('update/<slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<slug>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('to_published/<slug>', toggle_active, name='toggle_active')
]
