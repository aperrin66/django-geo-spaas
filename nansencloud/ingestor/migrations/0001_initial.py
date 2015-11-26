# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataLocation',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('catalog.datalocation',),
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('catalog.dataset',),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('catalog.source',),
        ),
    ]
