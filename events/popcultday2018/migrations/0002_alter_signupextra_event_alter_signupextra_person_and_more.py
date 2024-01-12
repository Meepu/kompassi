# Generated by Django 4.2.7 on 2023-11-26 09:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0039_alter_person_birth_date_alter_person_email_and_more"),
        ("enrollment", "0009_alter_enrollment_is_public_and_more"),
        ("popcultday2018", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signupextra",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="%(app_label)s_signup_extras", to="core.event"
            ),
        ),
        migrations.AlterField(
            model_name="signupextra",
            name="person",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, related_name="%(app_label)s_signup_extra", to="core.person"
            ),
        ),
        migrations.AlterField(
            model_name="signupextra",
            name="special_diet",
            field=models.ManyToManyField(
                blank=True,
                related_name="%(app_label)s_%(class)s",
                to="enrollment.specialdiet",
                verbose_name="Erikoisruokavalio",
            ),
        ),
    ]
