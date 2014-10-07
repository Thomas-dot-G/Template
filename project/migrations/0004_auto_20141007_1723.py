# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20141007_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='loser',
            field=models.ForeignKey(related_name=b'+', default=None, to='project.Player'),
        ),
        migrations.AlterField(
            model_name='match',
            name='winer',
            field=models.ForeignKey(related_name=b'+', default=None, to='project.Player'),
        ),
    ]
