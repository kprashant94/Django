# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsnalgo', '0002_auto_20160712_1830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ccode',
            old_name='code_file',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='javacode',
            old_name='code_file',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='pythoncode',
            old_name='code_file',
            new_name='code',
        ),
    ]
