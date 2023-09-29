from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from config import settings
from users.forms import UserCreationForm, UserUpdateForm
from users.models import User

import random


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        self.object = form.save()
        send_mail(
            subject='Регистрация нового пользователя',
            message='Поздравляем с регистрацией на сайте Django Shop Project!',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.object.email],
        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user


def reset_password(request):
    new_password = ''.join([str(random.randint(1, 9)) for _ in range(8)])
    request.user.set_password(new_password)
    request.user.save()
    send_mail(
        subject='Сброс пароля',
        message=f'Сброс пароля на сайте Django Shop Project\n\nВаш новый пароль {new_password}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[request.user.email],
    )
    return redirect(reverse_lazy('home'))
