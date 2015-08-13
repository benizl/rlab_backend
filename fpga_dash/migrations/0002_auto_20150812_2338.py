# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fpga_dash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('de2Serial', models.CharField(max_length=100)),
                ('ardSerial', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='DashSession',
        ),
    ]
