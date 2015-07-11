# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slam', '0003_judges_scores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round_1', models.ForeignKey(to='slam.Judges_scores')),
            ],
        ),
    ]
