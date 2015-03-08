# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masjid_data', '0003_auto_20150308_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='source',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='masjid',
            name='source',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='source',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
