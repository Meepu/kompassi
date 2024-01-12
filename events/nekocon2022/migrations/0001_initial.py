# Generated by Django 2.2.24 on 2022-02-22 19:16

import django.db.models.deletion
from django.db import migrations, models

import labour.models.signup_extras


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core", "0034_event_cancelled"),
    ]

    operations = [
        migrations.CreateModel(
            name="Night",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=63)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SpecialDiet",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=63)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SignupExtra",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("is_active", models.BooleanField(default=True)),
                (
                    "total_work",
                    models.CharField(
                        choices=[
                            ("8h", "8 tuntia"),
                            ("10h", "10–12 tuntia"),
                            ("yli12h", "Työn sankari! Yli 12 tuntia"),
                        ],
                        help_text="Kuinka paljon haluat tehdä töitä yhteensä tapahtuman aikana?",
                        max_length=15,
                        verbose_name="Toivottu kokonaistyömäärä",
                    ),
                ),
                (
                    "want_certificate",
                    models.BooleanField(default=False, verbose_name="Haluan todistuksen työskentelystäni Nekoconissa"),
                ),
                (
                    "afterparty_participation",
                    models.BooleanField(
                        default=False, verbose_name="Haluan osallistua kaatajaisiin sunnuntaina conin jälkeen"
                    ),
                ),
                (
                    "certificate_delivery_address",
                    models.TextField(
                        blank=True,
                        help_text="Jos haluat työtodistuksen, täytä tähän kenttään postiosoite (katuosoite, postinumero ja postitoimipaikka) johon haluat todistuksen toimitettavan.",
                        verbose_name="Työtodistuksen toimitusosoite",
                    ),
                ),
                (
                    "shirt_size",
                    models.CharField(
                        choices=[
                            ("NO_SHIRT", "Ei paitaa"),
                            ("XS", "XS Unisex"),
                            ("S", "S Unisex"),
                            ("M", "M Unisex"),
                            ("L", "L Unisex"),
                            ("XL", "XL Unisex"),
                            ("XXL", "XXL Unisex"),
                            ("3XL", "XXXL Unisex"),
                            ("LF_XS", "XS Ladyfit"),
                            ("LF_S", "S Ladyfit"),
                            ("LF_M", "M Ladyfit"),
                            ("LF_L", "L Ladyfit"),
                            ("LF_XL", "XL Ladyfit"),
                            ("LF_XXL", "XXL Ladyfit"),
                        ],
                        default="NO_SHIRT",
                        help_text="Ajoissa ilmoittautuneet vänkärit saavat maksuttoman työvoimapaidan.",
                        max_length=8,
                        verbose_name="Paidan koko",
                    ),
                ),
                (
                    "special_diet_other",
                    models.TextField(
                        blank=True,
                        help_text="Jos noudatat erikoisruokavaliota, jota ei ole yllä olevassa listassa, ilmoita se tässä. Tapahtuman järjestäjä pyrkii ottamaan erikoisruokavaliot huomioon, mutta kaikkia erikoisruokavalioita ei välttämättä pystytä järjestämään.",
                        verbose_name="Muu erikoisruokavalio",
                    ),
                ),
                (
                    "prior_experience",
                    models.TextField(
                        blank=True,
                        help_text="Kerro tässä kentässä, jos sinulla on aiempaa kokemusta vastaavista tehtävistä tai muuta sellaista työkokemusta, josta arvioit olevan hyötyä hakemassasi tehtävässä.",
                        verbose_name="Työkokemus",
                    ),
                ),
                (
                    "shift_wishes",
                    models.TextField(
                        blank=True,
                        help_text="Jos tiedät nyt jo, ettet pääse paikalle johonkin tiettyyn aikaan tai haluat osallistua johonkin tiettyyn ohjelmanumeroon, mainitse siitä tässä.",
                        verbose_name="Alustavat työvuorotoiveet",
                    ),
                ),
                (
                    "free_text",
                    models.TextField(
                        blank=True,
                        help_text="Jos haluat sanoa hakemuksesi käsittelijöille jotain sellaista, jolle ei ole omaa kenttää yllä, käytä tätä kenttää.",
                        verbose_name="Vapaa alue",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nekocon2022_signup_extras",
                        to="core.Event",
                    ),
                ),
                (
                    "lodging_needs",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Tarvitsetko majoitusta? Merkitse ne yöt, joille tarvitset majoituksen. Kerro vapaassa alueessa, mikäli toivot majoittuvasi luokassa, jossa on vain tyttöjä tai vain poikia.",
                        to="nekocon2022.Night",
                        verbose_name="Majoitustarve",
                    ),
                ),
                (
                    "person",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nekocon2022_signup_extra",
                        to="core.Person",
                    ),
                ),
                (
                    "special_diet",
                    models.ManyToManyField(blank=True, to="nekocon2022.SpecialDiet", verbose_name="Erikoisruokavalio"),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(labour.models.signup_extras.SignupExtraMixin, models.Model),
        ),
    ]
