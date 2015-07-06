# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slam', '0004_poet'),
    ]

    operations = [
        migrations.AddField(
            model_name='poet',
            name='round_2',
            field=models.ForeignKey(related_name='round_2', default=3, to='slam.Judges_scores'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poet',
            name='round_3',
            field=models.ForeignKey(related_name='round_3', default=2, to='slam.Judges_scores'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poet',
            name='round_1',
            field=models.ForeignKey(related_name='round_1', to='slam.Judges_scores'),
        ),
    ]
