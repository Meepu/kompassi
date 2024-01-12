# Generated by Django 4.2.7 on 2023-11-26 09:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("labour", "0036_alter_survey_event"),
        ("finncon2018", "0003_auto_20180611_1943"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signupextra",
            name="signup",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                related_name="%(app_label)s_signup_extra",
                serialize=False,
                to="labour.signup",
            ),
        ),
    ]
