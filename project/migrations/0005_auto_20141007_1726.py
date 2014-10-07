# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20141007_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='loser',
        ),
        migrations.RemoveField(
            model_name='match',
            name='winer',
        ),
        migrations.AlterField(
            model_name='player',
            name='matchs',
            field=models.ManyToManyField(related_name=b'participants', to=b'project.Match', blank=True),
        ),
    ]
