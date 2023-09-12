from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView

from catalog.models import *


class CatalogView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.get(pk=1)
        return context


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         Contacts.objects.create(name=name, phone=phone, message=message)
#         print(f'У вас новое сообщение от: {name}(телефон:{phone}): {message}')
#     return render(request, 'catalog/contacts.html', {'contacts': Contacts.objects.get(pk=1)})

class ProductView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


# def product(request, pk):
#     return render(request, 'catalog/product.html', {'product': Product.objects.get(pk=pk)})


class CategoryCreateView(CreateView):
    model = Category
    fields = ('name', 'description')
    template_name = 'catalog/cat_create.html'
    success_url = reverse_lazy('home')


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price', 'image', 'category')
    template_name = 'catalog/prod_create.html'
    success_url = reverse_lazy('home')


# def create_product(request):
#     if request.method == 'POST':
#         prod_category = request.POST.get('prod_category')
#         name = request.POST.get('prod_name')
#         price = request.POST.get('prod_price')
#         description = request.POST.get('prod_desc')
#         prod_image = request.FILES.get('prod_image')
#         Product.objects.create(name=name, description=description, price=price,
#                                image=prod_image, category=Category.objects.get(id=prod_category))
#         print(f"Данные:\n"
#               f"Название: {name}\n"
#               f"Описание: {description}\n"
#               f"Цена: {price}\n"
#               f"Фото: {prod_image}\n"
#               f"Категория: {prod_category}")
#     return render(request, 'catalog/prod_create.html', {'categories': Category.objects.all()})
