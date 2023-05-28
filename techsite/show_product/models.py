from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from category.models import Category


class product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена товара')
    content = models.TextField(blank=True, verbose_name='Описание')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'
