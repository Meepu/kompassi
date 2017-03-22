# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 21:36


import logging

from django.conf import settings
from django.db import migrations


logger = logging.getLogger('kompassi')


def populate_recipient_group_job_category(apps, schema_editor):
    JobCategory = apps.get_model('labour', 'jobcategory')
    RecipientGroup = apps.get_model('mailings', 'recipientgroup')

    for job_category in JobCategory.objects.filter():
        event = job_category.event

        group_name = '{installation_slug}-{host_slug}-{app_label}-{suffix}'.format(
            installation_slug=settings.KOMPASSI_INSTALLATION_SLUG,
            host_slug=event.slug,
            app_label='labour',
            suffix=job_category.slug,
        )

        try:
            recipient_group = RecipientGroup.objects.get(group__name=group_name)
        except RecipientGroup.DoesNotExist:
            logger.warn('Job category %s/%s has no recipient group', event.slug, job_category.slug)
        else:
            recipient_group.job_category = job_category
            recipient_group.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0004_recipientgroup_job_category'),
    ]

    operations = [
        migrations.RunPython(populate_recipient_group_job_category, elidable=True)
    ]
