# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crosspayapp', '0006_auto_20150529_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announce',
            old_name='detail',
            new_name='msg',
        ),
    ]
