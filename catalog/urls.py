from django.urls import path

from catalog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:pk>', views.product, name='product'),
    path('cat_create/', views.create_category, name='category_create'),
    path('product_create/', views.create_product, name='product_create'),
]
