# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crosspayapp', '0002_announce'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announce',
            name='author',
        ),
        migrations.RemoveField(
            model_name='announce',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='announce',
            name='foreignCity',
        ),
        migrations.RemoveField(
            model_name='announce',
            name='foreignCountry',
        ),
        migrations.RemoveField(
            model_name='announce',
            name='localCity',
        ),
        migrations.RemoveField(
            model_name='announce',
            name='localCountry',
        ),
        migrations.DeleteModel(
            name='Announce',
        ),
    ]
