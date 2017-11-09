# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='context',
            field=models.TextField(verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.CharField(max_length=30, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
    ]
