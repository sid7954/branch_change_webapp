# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branchchange', '0012_auto_20151028_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchchangeform',
            name='department',
            field=models.CharField(default=1, max_length=1, choices=[(1, b'AE B.Tech'), (2, b'CE B.Tech'), (3, b'CH'), (4, b'CL B.Tech'), (5, b'CL Dual Deg'), (6, b'CS B.Tech'), (7, b'EE B.Tech'), (8, b'EE Dual Deg E1'), (9, b'EE Dual Deg E2'), (10, b'EN Dual Deg'), (11, b'EP B.Tech'), (12, b'EP Dual Deg N1'), (13, b'ME B.Tech'), (14, b'ME Dual Deg M2'), (15, b'MM B.Tech'), (16, b'MM Dual Deg Y1'), (17, b'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='inputbranchlist',
            name='input_file',
            field=models.FileField(upload_to=b'/home/sanat/Desktop/Python Projects/Branch_Change/django/src'),
        ),
        migrations.AlterField(
            model_name='inputstudentpreferrencelist',
            name='input_file',
            field=models.FileField(upload_to=b'/home/sanat/Desktop/Python Projects/Branch_Change/django/src'),
        ),
    ]
