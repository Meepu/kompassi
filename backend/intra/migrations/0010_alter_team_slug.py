# Generated by Django 5.0.9 on 2024-11-30 15:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intra", "0009_intraeventmeta_is_organizer_list_public"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="slug",
            field=models.CharField(
                help_text='Tekninen nimi eli "slug" näkyy URL-osoitteissa. Sallittuja merkkejä ovat pienet kirjaimet, numerot ja väliviiva. Teknistä nimeä ei voi muuttaa luomisen jälkeen.',
                max_length=255,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Tekninen nimi saa sisältää vain pieniä kirjaimia, numeroita sekä väliviivoja.",
                        regex="^[a-z0-9-]+$",
                    )
                ],
                verbose_name="Tekninen nimi",
            ),
        ),
    ]