# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masjid_data', '0006_auto_20150308_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='address',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
