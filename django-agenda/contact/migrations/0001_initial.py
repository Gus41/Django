# Generated by Django 5.0.6 on 2024-06-25 09:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
            ],
        ),
    ]
