# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crosspayapp', '0004_announce'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='detail',
            field=models.CharField(max_length=160, null=True, blank=True),
        ),
    ]
