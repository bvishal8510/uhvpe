# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20171125_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='branch',
            field=models.CharField(choices=[(None, '----'), ('MCA', 'MCA'), ('MBA', 'MBA'), ('CS', 'CS'), ('IT', 'IT'), ('ECE', 'ECE'), ('EN', 'EN'), ('ME', 'ME'), ('EI', 'EI'), ('CE', 'CE')], default=None, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='student_no',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='year',
            field=models.IntegerField(choices=[(None, '----'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], default=None, null=True),
        ),
    ]