# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crosspayapp', '0003_auto_20150529_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=12, decimal_places=3)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(max_length=15, blank=True)),
                ('completed', models.BooleanField(default=False)),
                ('completedDate', models.DateTimeField(null=True, blank=True)),
                ('detail', models.CharField(max_length=160)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('currency', models.ForeignKey(to='crosspayapp.Currency')),
                ('foreignCity', models.ForeignKey(to='crosspayapp.City')),
                ('foreignCountry', models.ForeignKey(to='crosspayapp.Country')),
                ('localCity', models.ForeignKey(related_name='+', to='crosspayapp.City')),
                ('localCountry', models.ForeignKey(related_name='+', to='crosspayapp.Country')),
            ],
        ),
    ]
