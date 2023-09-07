from django.shortcuts import render, redirect
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


def create_category(request):
    if request.method == 'POST':
        cat_name = request.POST.get('cat_name')
        cat_desc = request.POST.get('cat_desc')
        Category.objects.create(name=cat_name, description=cat_desc)
        return redirect('home')
    return render(request, 'catalog/cat_create.html')


def create_product(request):
    if request.method == 'POST':
        prod_category = request.POST.get('prod_category')
        name = request.POST.get('prod_name')
        price = request.POST.get('prod_price')
        description = request.POST.get('prod_desc')
        prod_image = request.FILES.get('prod_image')
        Product.objects.create(name=name, description=description, price=price,
                               image=prod_image, category=Category.objects.get(id=prod_category))
        print(f"Данные:\n"
              f"Название: {name}\n"
              f"Описание: {description}\n"
              f"Цена: {price}\n"
              f"Фото: {prod_image}\n"
              f"Категория: {prod_category}")
    return render(request, 'catalog/prod_create.html', {'categories': Category.objects.all()})
