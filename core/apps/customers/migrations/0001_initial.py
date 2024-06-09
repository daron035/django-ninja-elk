# Generated by Django 5.0.6 on 2024-06-09 02:10

import uuid

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('phone', models.CharField(max_length=20, unique=True, verbose_name='Phone Number')),
                ('token', models.CharField(default=uuid.uuid4, max_length=255, unique=True, verbose_name='User Token')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
    ]