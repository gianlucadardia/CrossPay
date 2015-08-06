# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crosspayapp', '0008_activation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='dialing_code',
            field=models.CharField(max_length=15),
        ),
    ]
