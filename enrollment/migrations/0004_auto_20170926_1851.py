# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-26 15:51
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0003_auto_20170417_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='concon_event_affiliation',
            field=models.CharField(blank=True, default='', help_text='Mikäli edustat jotain tapahtumaorganisaatiota, voit kertoa siitä tässä. Conconiin ovat tervetulleita osallistumaan kaikki kiinnostuneet, eli minkään tapahtumaorganisaation edustaminen ei ole edellytys osallistumiselle.', max_length=512, verbose_name='Mitä tapahtumia edustat?'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enrollment',
            name='is_public',
            field=models.NullBooleanField(choices=[(True, 'Sallin nimeni julkaisemisen osallistujalistassa'), (False, 'Kiellän nimeni julkaisemisen osallistujalistassa')], help_text='Tästä tapahtumasta julkistetaan osallistujalista, jossa näkyvät niiden osallistujien nimet, jotka ovat antaneet siihen luvan. Nimesi näytetään valitsemassasi muodossa, jonka voit tarkistaa ja muuttaa <a href="/profile" target="_blank">profiilissasi.</a>.', verbose_name='Näkyminen osallistujalistassa'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='state',
            field=models.CharField(choices=[('NEW', 'New'), ('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected'), ('CANCELLED', 'Cancelled')], default='ACCEPTED', max_length=9, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='enrollmenteventmeta',
            name='initial_state',
            field=models.CharField(choices=[('NEW', 'New'), ('ACCEPTED', 'Accepted')], default='ACCEPTED', help_text='Change this to New to require approval for new enrollments.', max_length=8, verbose_name='Initial state'),
        ),
        migrations.AddField(
            model_name='enrollmenteventmeta',
            name='is_participant_list_public',
            field=models.BooleanField(default=False, help_text='If this option is selected, the names of participants who have given the permission to do so will be published.', verbose_name='Participant list is public'),
        ),
    ]
