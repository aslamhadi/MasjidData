# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masjid_data', '0004_auto_20150308_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='room_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
