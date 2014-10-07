# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20141007_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match', models.ForeignKey(to='project.Match')),
                ('player', models.ForeignKey(to='project.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='player',
            name='matchs',
        ),
        migrations.AddField(
            model_name='match',
            name='scores',
            field=models.ManyToManyField(to='project.Player', through='project.Score', blank=True),
            preserve_default=True,
        ),
    ]
