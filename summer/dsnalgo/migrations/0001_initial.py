# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='CCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_file', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='JavaCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_file', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='PythonCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_file', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='SubArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('article', models.ForeignKey(to='dsnalgo.Article')),
            ],
        ),
        migrations.AddField(
            model_name='pythoncode',
            name='sub_article',
            field=models.ForeignKey(to='dsnalgo.SubArticle'),
        ),
        migrations.AddField(
            model_name='javacode',
            name='sub_article',
            field=models.ForeignKey(to='dsnalgo.SubArticle'),
        ),
        migrations.AddField(
            model_name='ccode',
            name='sub_article',
            field=models.ForeignKey(to='dsnalgo.SubArticle'),
        ),
    ]
