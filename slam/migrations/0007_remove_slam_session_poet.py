# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slam', '0006_poet_slam_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slam_session',
            name='poet',
        ),
    ]
