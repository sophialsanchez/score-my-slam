# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slam', '0003_delete_poet'),
    ]

    operations = [
        migrations.AddField(
            model_name='slam_session',
            name='poet',
            field=models.CharField(default='poet', max_length=200),
            preserve_default=False,
        ),
    ]
