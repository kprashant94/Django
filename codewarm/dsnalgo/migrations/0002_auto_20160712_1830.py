# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsnalgo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccode',
            name='code_file',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='javacode',
            name='code_file',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='pythoncode',
            name='code_file',
            field=models.TextField(max_length=5000),
        ),
    ]
