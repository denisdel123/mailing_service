# Generated by Django 5.0.3 on 2024-04-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailingApp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(choices=[('create', 'Создана'), ('completed', 'Завершена'), ('launched', 'Запущена')], default='create', max_length=20, verbose_name='Статус'),
        ),
    ]
