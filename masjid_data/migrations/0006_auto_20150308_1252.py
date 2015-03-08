# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masjid_data', '0005_hotel_room_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='is_free_wifi',
        ),
        migrations.AddField(
            model_name='hotel',
            name='wifi',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='wifi',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hotel',
            name='room_count',
            field=models.CharField(default=b'0', max_length=20),
            preserve_default=True,
        ),
    ]
