from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(verbose_name='Изображение', upload_to='img/', **NULLABLE)
    category = models.CharField(verbose_name='Категория', max_length=100)
    price = models.IntegerField(verbose_name='Цена', **NULLABLE)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_modified = models.DateTimeField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='Поле_для_дальнейшего_удаления', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
