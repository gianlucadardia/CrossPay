# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crosspayapp', '0005_auto_20150529_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='detail',
            field=models.TextField(max_length=160, null=True, blank=True),
        ),
    ]
