# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-17 19:59
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popcult2017', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupextra',
            name='special_diet',
            field=models.ManyToManyField(blank=True, related_name='popcult2017_signupextra', to='enrollment.SpecialDiet', verbose_name='Erikoisruokavalio'),
        ),
    ]
