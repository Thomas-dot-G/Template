# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='loser',
            field=models.ForeignKey(related_name=b'lose', default=None, to='project.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='winer',
            field=models.ForeignKey(related_name=b'win', default=None, to='project.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='matchs',
            field=models.ManyToManyField(to='project.Match'),
            preserve_default=True,
        ),
    ]
