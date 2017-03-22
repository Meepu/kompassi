# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-16 11:19


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracon11', '0003_signupextra_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupextra',
            name='shift_wishes',
            field=models.TextField(blank=True, help_text='Jos tied\xe4t, ettet p\xe4\xe4se paikalle johonkin tiettyyn aikaan tai haluat esimerkiksi osallistua johonkin tiettyyn ohjelmanumeroon, mainitse siit\xe4 t\xe4ss\xe4.', verbose_name='Ty\xf6vuorotoiveet'),
        ),
        migrations.AlterField(
            model_name='signupextra',
            name='shift_type',
            field=models.CharField(choices=[('yksipitka', 'Yksi pitk\xe4 vuoro'), ('montalyhytta', 'Monta lyhyemp\xe4\xe4 vuoroa'), ('kaikkikay', 'Kumpi tahansa k\xe4y')], help_text='Haluatko tehd\xe4 yhden pitk\xe4n ty\xf6vuoron vaiko monta lyhyemp\xe4\xe4 vuoroa?', max_length=15, verbose_name='Toivottu ty\xf6vuoron pituus'),
        ),
        migrations.AlterField(
            model_name='signupextra',
            name='total_work',
            field=models.CharField(choices=[('8h', 'Minimi - 8 tuntia (1 l\xe4mmin ateria)'), ('12h', '12 tuntia (2 l\xe4mmint\xe4 ateriaa)'), ('yli12h', 'Ty\xf6n Sankari! Yli 12 tuntia! (2 l\xe4mmint\xe4 ateriaa)')], help_text='Kuinka paljon haluat tehd\xe4 t\xf6it\xe4 yhteens\xe4 tapahtuman aikana? Useimmissa teht\xe4vist\xe4 minimi on kahdeksan tuntia, mutta joissain teht\xe4viss\xe4 se voi olla my\xf6s v\xe4hemm\xe4n (esim. majoitusvalvonta 6 h).', max_length=15, verbose_name='Toivottu kokonaisty\xf6m\xe4\xe4r\xe4'),
        ),
    ]
