# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 20:30


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0013_make_personnel_class_mandatory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='first_name',
            field=models.CharField(blank=True, max_length=1023, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='badge',
            name='surname',
            field=models.CharField(blank=True, max_length=1023, verbose_name='Surname'),
        ),
    ]
