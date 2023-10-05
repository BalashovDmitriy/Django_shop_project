from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import CatalogView, ContactsView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, categories, CategoryDetailView

urlpatterns = [
    path('', CatalogView.as_view(), name='home'),
    path('contacts/', cache_page(60)(ContactsView.as_view()), name='contacts'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('categories/', categories, name='categories'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
