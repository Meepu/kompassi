# Generated by Django 5.0.8 on 2024-08-18 16:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0039_alter_ticketseventmeta_terms_and_conditions_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ticketseventmeta",
            name="reservation_seconds",
        ),
    ]
