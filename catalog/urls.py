from django.urls import path

from catalog.views import CatalogView, ContactsView, ProductView, CategoryCreateView, ProductCreateView

urlpatterns = [
    path('', CatalogView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductView.as_view(), name='product'),
    path('cat_create/', CategoryCreateView.as_view(), name='category_create'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
]
