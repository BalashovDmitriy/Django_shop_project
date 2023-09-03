from django.db import models


# Create your models here.
class Product(models.Model):

    class Meta:
        verbose_name = 'Наименование'
        verbose_name_plural = 'Наименования'


class Category(models.Model):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
