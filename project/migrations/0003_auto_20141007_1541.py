# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20141007_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='matchs',
            field=models.ManyToManyField(to=b'project.Match', blank=True),
        ),
    ]
