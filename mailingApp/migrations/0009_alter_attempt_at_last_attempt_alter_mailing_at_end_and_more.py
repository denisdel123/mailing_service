# Generated by Django 5.0.3 on 2024-03-27 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailingApp', '0008_alter_mailing_at_end_alter_mailing_at_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='at_last_attempt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата последней попытки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='at_end',
            field=models.DateField(verbose_name='Дата окончания отправки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='at_start',
            field=models.DateField(verbose_name='Дата начала отправки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(choices=[('launched', 'Запущена'), ('completed', 'Завершена'), ('create', 'Создана')], default='create', max_length=20, verbose_name='Статус'),
        ),
    ]