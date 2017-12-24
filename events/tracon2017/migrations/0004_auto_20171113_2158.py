# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-13 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracon2017', '0003_auto_20170912_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupextra',
            name='pick_your_poison',
            field=models.ManyToManyField(blank=True, help_text='Pyrimme siihen, että kaikki löytäisivät kaadon tarjoiluista jotain itselleen sopivaa. Ruksaa kaikki ne juomat, mitä saattaisit kuvitella nauttivasi kaadon aikana, niin yritämme arvioida määriä jotenkin sinne päin. Huomaathan, että haluamme kuitenkin pitää kaadon kaikille mukavana ja turvallisena, eikä kaadossa ole tarkoitus juoda itseään örveltäväksi idiootiksi.', to='tracon2017.Poison', verbose_name='Mitä tykkäät juoda?'),
        ),
    ]