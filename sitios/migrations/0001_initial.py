# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sitio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(help_text='Sitio a monitorear. Ej. https://www.google.com/', verbose_name='URL')),
                ('frecuencia', models.IntegerField(default=10, help_text='Frecuencia de monitoreo en segundos')),
                ('timeout', models.IntegerField(default=10, help_text='Timeout en segundos.')),
            ],
        ),
    ]