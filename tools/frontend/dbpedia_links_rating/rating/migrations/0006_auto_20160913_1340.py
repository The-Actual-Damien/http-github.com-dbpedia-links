# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-13 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0005_auto_20160913_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='link',
            name='object_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='rating',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='object_id',
            field=models.PositiveIntegerField(),
        ),
    ]