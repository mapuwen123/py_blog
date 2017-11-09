# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 07:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171109_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='blog.Articles')),
                ('content', models.TextField(verbose_name='内容')),
            ],
        ),
    ]
