# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20180214_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(default=None, upload_to=b''),
        ),
    ]
