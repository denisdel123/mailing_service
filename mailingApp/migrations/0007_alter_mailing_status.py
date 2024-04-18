# Generated by Django 5.0.3 on 2024-04-18 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailingApp', '0006_alter_mailing_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(choices=[('completed', 'Завершена'), ('create', 'Создана'), ('launched', 'Запущена')], default='create', max_length=20, verbose_name='Статус'),
        ),
    ]