# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 21:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_course_has_prerequisites'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Savings'), (2, 'Credit'), (3, 'Goal')], db_index=True, default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='has_prerequisites',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]