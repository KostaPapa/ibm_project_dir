# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-17 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_task', '0004_auto_20180516_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TASK_NOT_COMPLETED', 'Not completed Task'), ('TASK_COMPLETED', 'Completed Task')], default='TASK_NOT_COMPLETED', max_length=30),
        ),
    ]
