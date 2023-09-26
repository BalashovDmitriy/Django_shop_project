from django.urls import path

from catalog.views import CatalogView, ContactsView, ProductDetailView, CategoryCreateView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', CatalogView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('cat_create/', CategoryCreateView.as_view(), name='category_create'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
