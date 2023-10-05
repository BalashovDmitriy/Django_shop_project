from django.urls import path

from catalog.views import CatalogView, ContactsView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryListView, CategoryDetailView

urlpatterns = [
    path('', CatalogView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
