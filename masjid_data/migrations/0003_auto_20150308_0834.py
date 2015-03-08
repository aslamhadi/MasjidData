# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masjid_data', '0002_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=255)),
                ('cuisine', models.CharField(max_length=255)),
                ('halal_cert', models.CharField(max_length=255)),
                ('alcohol_beverage', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('dine_in', models.BooleanField(default=False)),
                ('take_away', models.BooleanField(default=False)),
                ('cc_accepted', models.BooleanField(default=False)),
                ('seat', models.IntegerField(default=0)),
                ('tel', models.CharField(default=b'', max_length=50)),
                ('fax', models.CharField(default=b'', max_length=100)),
                ('email', models.CharField(default=b'', max_length=100)),
                ('website', models.CharField(default=b'', max_length=200)),
                ('price', models.CharField(default=b'', max_length=255)),
                ('other', models.CharField(default=b'', max_length=255)),
                ('lang', models.CharField(default=b'', max_length=255)),
                ('is_item_prayer', models.BooleanField(default=False)),
                ('is_prayer_room', models.BooleanField(default=False)),
                ('is_free_wifi', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='hotel',
            name='lang',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
