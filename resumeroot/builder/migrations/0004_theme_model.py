# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-06 11:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0003_auto_20171211_0514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme_Model',
            fields=[
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='builder.Resume', unique=True)),
                ('theme', models.CharField(choices=[(0, 'standard'), (1, 'express'), (2, 'compact')], default='standard', max_length=6)),
                ('font_size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('font_family', models.CharField(choices=[(0, 'computer modern'), (1, 'arial'), (2, 'calibri')], default='computer modern', max_length=6)),
                ('horizontal_margins', models.DecimalField(decimal_places=2, max_digits=5)),
                ('top_margin', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bottom_margin', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
