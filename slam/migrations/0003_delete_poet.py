# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slam', '0002_remove_poet_slam_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Poet',
        ),
    ]
