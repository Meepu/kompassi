# Generated by Django 1.9.1 on 2016-01-25 21:47


import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("programme", "0015_auto_20160125_2328"),
    ]

    operations = [
        migrations.CreateModel(
            name="FreeformOrganizer",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "text",
                    models.CharField(
                        help_text="This text will be shown as-is in the schedule", max_length=255, verbose_name="Text"
                    ),
                ),
                (
                    "programme",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="freeform_organizers",
                        to="programme.Programme",
                        verbose_name="Programme",
                    ),
                ),
            ],
            options={
                "verbose_name": "freeform organizer",
                "verbose_name_plural": "freeform organizers",
            },
        ),
    ]
