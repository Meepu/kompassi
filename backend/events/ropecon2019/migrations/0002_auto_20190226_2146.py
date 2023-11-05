# Generated by Django 2.1.5 on 2019-02-26 19:46

import django.db.models.deletion
from django.db import migrations, models

import labour.models.signup_extras


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0030_auto_20180926_1252"),
        ("ropecon2019", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SignupExtra",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "shift_type",
                    models.CharField(
                        choices=[
                            ("yksipitka", "Yksi pitkä vuoro"),
                            ("montalyhytta", "Monta lyhyempää vuoroa"),
                            ("kaikkikay", "Kumpi tahansa käy"),
                        ],
                        help_text="Haluatko tehdä yhden pitkän työvuoron vaiko monta lyhyempää vuoroa?",
                        max_length=15,
                        verbose_name="Toivottu työvuoron pituus",
                    ),
                ),
                (
                    "total_work",
                    models.CharField(
                        choices=[
                            ("8h", "Minimi - 8 tuntia"),
                            ("12h", "10–12 tuntia"),
                            ("yli12h", "Työn Sankari! Yli 12 tuntia!"),
                        ],
                        help_text="Kuinka paljon haluat tehdä töitä yhteensä tapahtuman aikana? Useimmissa tehtävistä minimi on kahdeksan tuntia, mutta joissain tehtävissä se voi olla myös vähemmän (esim. majoitusvalvonta 6 h).",
                        max_length=15,
                        verbose_name="Toivottu kokonaistyömäärä",
                    ),
                ),
                (
                    "want_certificate",
                    models.BooleanField(default=False, verbose_name="Haluan todistuksen työskentelystäni Ropeconissa"),
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
                ("is_active", models.BooleanField(default=True)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ropecon2019_signup_extras",
                        to="core.Event",
                    ),
                ),
                (
                    "person",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ropecon2019_signup_extra",
                        to="core.Person",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(labour.models.signup_extras.SignupExtraMixin, models.Model),
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
        migrations.AddField(
            model_name="signupextra",
            name="special_diet",
            field=models.ManyToManyField(blank=True, to="ropecon2019.SpecialDiet", verbose_name="Erikoisruokavalio"),
        ),
    ]