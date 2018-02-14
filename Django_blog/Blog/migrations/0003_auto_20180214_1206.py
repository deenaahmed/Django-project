# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20180214_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category_subscribe',
            name='status',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
