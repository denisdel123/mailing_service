from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='активация')
    is_confirm = models.BooleanField(default=False, verbose_name='подтверждение почты')
    code = models.CharField(max_length=15, **NULLABLE, default=None, verbose_name='проверочный код')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        permissions = [
            (
                'set_active',
                'Can block user'
            )
        ]
