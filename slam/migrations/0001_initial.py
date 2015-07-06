# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slam_session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slam_name', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name=b'date published')),
                ('number_of_rounds', models.IntegerField()),
                ('number_of_judges', models.IntegerField()),
                ('poet_1', models.CharField(max_length=200)),
                ('poet_2', models.CharField(max_length=200)),
                ('poet_3', models.CharField(max_length=200)),
            ],
        ),
    ]
