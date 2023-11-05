# Generated by Django 2.2.27 on 2022-03-13 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("programme", "0107_auto_20220221_2251"),
    ]

    operations = [
        migrations.AlterField(
            model_name="programme",
            name="ropecon2022_aimed_at_adult_participants",
            field=models.BooleanField(
                default=False,
                help_text="Tick this box if your programme is designed for adult participants.",
                verbose_name="Aimed at adult participants",
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="ropecon2022_aimed_at_children_under_10",
            field=models.BooleanField(
                default=False,
                help_text="Tick this box if your programme is designed for children under the age of 10.",
                verbose_name="Aimed at children under 10 years old",
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="ropecon2022_aimed_at_underage_participants",
            field=models.BooleanField(
                default=False,
                help_text="Tick this box if your programme is designed for underage participants.",
                verbose_name="Aimed at underage participants",
            ),
        ),
    ]