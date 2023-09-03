from django.contrib import admin

from catalog.models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    text_fields = ('name', 'description', 'price', 'image',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    text_fields = ('name',)
