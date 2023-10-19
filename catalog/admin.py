from django.contrib import admin

from catalog.models import *
from users.models import User


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'is_published')
    list_filter = ('category',)
    list_editable = ('description', 'category', 'is_published')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number_version', 'name_version', 'current_version')


admin.site.register(Contacts)
admin.site.register(User)
