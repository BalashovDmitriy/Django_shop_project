from django.core.cache import cache
from django.core.mail import send_mail

from catalog.models import Category
from config.settings import CACHE_ENABLED


def categories_get_cache():
    key = 'category_list'
    if CACHE_ENABLED:
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()
    return category_list


def send_message_mail(obj):
    send_mail(
        subject='У вас новое сообщение',
        message=f'{obj}\n{obj.message}',
        from_email='reaver74@yandex.ru',
        recipient_list=['reaver_std@mail.ru'],
        fail_silently=False
    )
