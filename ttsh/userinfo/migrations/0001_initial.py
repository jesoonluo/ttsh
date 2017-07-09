# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=20)),
                ('user_pwd', models.CharField(max_length=40)),
                ('user_mail', models.CharField(max_length=20)),
                ('receiver', models.CharField(max_length=20)),
                ('receiver_phone', models.CharField(max_length=11)),
                ('receiver_addr', models.CharField(max_length=100)),
                ('receiver_code', models.CharField(max_length=6)),
            ],
        ),
    ]
