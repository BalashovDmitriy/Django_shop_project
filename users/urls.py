from django.urls import path

from users.views import LoginView, LogoutView, UserCreateView, UserUpdateView, reset_password

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/reset_password/', reset_password, name='reset_password'),
]