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


class ProductView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


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
