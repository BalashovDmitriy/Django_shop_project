from django.shortcuts import render
from catalog.models import *


def home(request):
    print(Product.objects.all()[::-1][:5])
    return render(request, 'catalog/home.html', {'products': Product.objects.all()})


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Contacts.objects.create(name=name, phone=phone, message=message)
        print(f'У вас новое сообщение от: {name}(телефон:{phone}): {message}')
    return render(request, 'catalog/contacts.html', {'contacts': Contacts.objects.get(pk=1)})


def product(request, pk):
    return render(request, 'catalog/product.html', {'product': Product.objects.get(pk=pk)})
