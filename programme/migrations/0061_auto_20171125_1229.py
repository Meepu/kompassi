# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-25 10:29
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0060_auto_20171113_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='view_rooms', to='programme.Room')),
                ('view', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='view_rooms', to='programme.View')),
            ],
            options={
                'ordering': ['view', 'order'],
            },
        ),
        migrations.AlterField(
            model_name='programme',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='programmes', to='programme.Room', verbose_name='Room'),
        ),
    ]
