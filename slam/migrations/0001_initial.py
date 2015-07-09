# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Judges_scores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score_1', models.FloatField(max_length=50, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('score_2', models.FloatField(max_length=50, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('score_3', models.FloatField(max_length=50, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('score_4', models.FloatField(max_length=50, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('score_5', models.FloatField(max_length=50, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Poet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('poet_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Slam_session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slam_name', models.CharField(max_length=200)),
                ('number_of_rounds', models.IntegerField()),
                ('number_of_judges', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='poet',
            name='slam_details',
            field=models.ForeignKey(blank=True, to='slam.Slam_session', null=True),
        ),
    ]
