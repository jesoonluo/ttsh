# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodsinfo', '0001_initial'),
        ('userinfo', '0002_auto_20170709_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='goodsinfo.GoodsInfo')),
                ('user', models.ForeignKey(to='userinfo.UserInfo')),
            ],
        ),
    ]
