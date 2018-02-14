# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_auto_20180214_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dislikes',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=b'0'),
        ),
    ]
