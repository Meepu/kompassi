# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 19:40


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0008_auto_20160129_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='first_name',
            field=models.CharField(max_length=1023, null=True, verbose_name='First name'),
        ),
        migrations.AddField(
            model_name='badge',
            name='is_first_name_visible',
            field=models.BooleanField(default=True, verbose_name='Is first_name visible'),
        ),
        migrations.AddField(
            model_name='badge',
            name='is_nick_visible',
            field=models.BooleanField(default=True, verbose_name='Is nick visible'),
        ),
        migrations.AddField(
            model_name='badge',
            name='is_surname_visible',
            field=models.BooleanField(default=True, verbose_name='Is surname visible'),
        ),
        migrations.AddField(
            model_name='badge',
            name='nick',
            field=models.CharField(blank=True, help_text='Nick name', max_length=1023, null=True),
        ),
        migrations.AddField(
            model_name='badge',
            name='surname',
            field=models.CharField(max_length=1023, null=True, verbose_name='Surname'),
        ),
    ]
