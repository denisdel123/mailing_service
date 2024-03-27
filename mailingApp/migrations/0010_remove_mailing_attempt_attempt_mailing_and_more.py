# Generated by Django 5.0.3 on 2024-03-27 10:07

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailingApp', '0009_alter_attempt_at_last_attempt_alter_mailing_at_end_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='attempt',
        ),
        migrations.AddField(
            model_name='attempt',
            name='mailing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailingApp.mailing', verbose_name='Рассылка'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='next_run',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 10, 7, 3, 320032, tzinfo=datetime.timezone.utc), verbose_name='Дата и время отправки'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(choices=[('create', 'Создана'), ('launched', 'Запущена'), ('completed', 'Завершена')], default='create', max_length=20, verbose_name='Статус'),
        ),
    ]