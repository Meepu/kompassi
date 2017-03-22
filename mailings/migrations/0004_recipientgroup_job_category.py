# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 21:30


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labour', '0019_auto_20160207_2330'),
        ('mailings', '0003_message_channel_help'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipientgroup',
            name='job_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='labour.JobCategory'),
        ),
    ]
