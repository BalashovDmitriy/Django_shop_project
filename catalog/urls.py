from django.urls import path, include

urlpatterns = [
    path('catalog', include('catalog.urls')),
]
