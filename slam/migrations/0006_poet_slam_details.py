# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slam', '0005_poet'),
    ]

    operations = [
        migrations.AddField(
            model_name='poet',
            name='slam_details',
            field=models.ForeignKey(related_name='slam_session', blank=True, to='slam.Slam_session', null=True),
        ),
    ]
