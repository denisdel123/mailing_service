# Generated by Django 5.0.3 on 2024-04-15 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('set_active', 'Can block user')]},
        ),
    ]