# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='receiver',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='receiver_addr',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='receiver_code',
            field=models.CharField(default=b'', max_length=6),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='receiver_phone',
            field=models.CharField(default=b'', max_length=11),
        ),
    ]
