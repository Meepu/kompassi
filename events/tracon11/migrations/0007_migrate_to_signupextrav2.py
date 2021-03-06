# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-13 13:04


from django.db import migrations


SCALAR_FIELDS = [
    'shift_type',
    'total_work',
    'overseer',
    'want_certificate',
    'certificate_delivery_address',
    'shirt_size',
    'special_diet_other',
    'prior_experience',
    'free_text',
    'shift_wishes',
    'email_alias',
]

M2M_FIELDS = [
    'special_diet',
    'lodging_needs',
]


def migrate_to_signupextra_v2(apps, schema_editor):
    SignupExtra = apps.get_model('tracon11', 'signupextra')
    SignupExtraV2 = apps.get_model('tracon11', 'signupextrav2')
    LabourEventMeta = apps.get_model('labour', 'laboureventmeta')
    ContentType = apps.get_model('contenttypes', 'contenttype')

    for signup_extra in SignupExtra.objects.all():
        event = signup_extra.signup.event
        person = signup_extra.signup.person

        try:
            signup_extra_v2 = SignupExtraV2.objects.get(event=event, person=person)
        except SignupExtraV2.DoesNotExist:
            signup_extra_v2 = SignupExtraV2(event=event, person=person)

            for scalar_field_name in SCALAR_FIELDS:
                value = getattr(signup_extra, scalar_field_name)
                setattr(signup_extra_v2, scalar_field_name, value)

            signup_extra_v2.save()

            for m2m_field_name in M2M_FIELDS:
                manager = getattr(signup_extra, m2m_field_name)
                manager_v2 = getattr(signup_extra_v2, m2m_field_name)
                manager_v2.set(manager.all())

    try:
        meta = LabourEventMeta.objects.get(event__slug='tracon11')
    except LabourEventMeta.DoesNotExist:
        # Clean install
        pass
    else:
        signup_extra_v2_content_type = ContentType.objects.get_for_model(SignupExtraV2)
        meta.signup_extra_content_type = signup_extra_v2_content_type
        meta.save()


class Migration(migrations.Migration):

    dependencies = [
        ('tracon11', '0006_signupextrav2'),
    ]

    operations = [
        migrations.RunPython(migrate_to_signupextra_v2, elidable=True),
    ]
