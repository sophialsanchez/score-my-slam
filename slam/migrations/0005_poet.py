# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slam', '0004_slam_session_poet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('poet_name', models.CharField(max_length=200)),
            ],
        ),
    ]
