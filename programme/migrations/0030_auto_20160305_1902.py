# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-05 17:02


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0029_room_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='extra_invites',
            field=models.PositiveIntegerField(default=0, help_text='The host may send this many extra invites to other hosts of the programme.', verbose_name='Extra invites'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='sire',
            field=models.ForeignKey(blank=True, help_text='The host that spawned this invitation. Sired invitations consume the extra invite quota of the sire.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sired_invitation_set', to='programme.ProgrammeRole', verbose_name='Sire'),
        ),
        migrations.AddField(
            model_name='programmerole',
            name='extra_invites',
            field=models.PositiveIntegerField(default=0, help_text='The host may send this many extra invites to other hosts of the programme.', verbose_name='Extra invites'),
        ),
    ]
