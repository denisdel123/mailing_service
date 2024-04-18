from django.db import models

from mailingApp.models import NULLABLE
from usersApp.models import User


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Изображение')
    view_count = models.IntegerField(default=0, verbose_name='Просмотры')
    at_published = models.DateTimeField(**NULLABLE, verbose_name='Дата публикации')
    at_create = models.DateTimeField(auto_now_add=True, **NULLABLE, verbose_name='Дата создания блога')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Собственник')
    is_published = models.BooleanField(default=False, verbose_name='Статус публикации')
    slug = models.SlugField(max_length=50, **NULLABLE, verbose_name='slug')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
