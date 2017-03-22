# encoding: utf-8

from django.db import models

from labour.models import ObsoleteSignupExtraBaseV1
from labour.querybuilder import QueryBuilder, add_prefix

from core.utils import validate_slug


SHIRT_SIZES = [
    ('NO_SHIRT', 'Ei paitaa'),

    ('XS', 'XS Unisex'),
    ('S', 'S Unisex'),
    ('M', 'M Unisex'),
    ('L', 'L Unisex'),
    ('XL', 'XL Unisex'),
    ('XXL', 'XXL Unisex'),
    ('3XL', '3XL Unisex'),
    ('4XL', '4XL Unisex'),
    ('5XL', '5XL Unisex'),

    ('LF_XS', 'XS Ladyfit'),
    ('LF_S', 'S Ladyfit'),
    ('LF_M', 'M Ladyfit'),
    ('LF_L', 'L Ladyfit'),
    ('LF_XL', 'XL Ladyfit'),
]

SHIFT_TYPE_CHOICES = [
    ('yksipitka', 'Yksi pitkä vuoro'),
    ('montalyhytta', 'Monta lyhyempää vuoroa'),
    ('kaikkikay', 'Kumpi tahansa käy'),
]

TOTAL_WORK_CHOICES = [
    ('8h', 'Minimi - 8 tuntia (1 lämmin ateria)'),
    ('12h', '12 tuntia (2 lämmintä ateriaa)'),
    ('yli12h', 'Työn Sankari! Yli 12 tuntia! (2 lämmintä ateriaa)'),
]


class SimpleChoice(models.Model):
    name = models.CharField(max_length=63)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class SpecialDiet(SimpleChoice):
    pass


class Night(SimpleChoice):
    pass


class SignupExtra(ObsoleteSignupExtraBaseV1):
    shift_type = models.CharField(max_length=15,
        verbose_name='Toivottu työvuoron pituus',
        help_text='Haluatko tehdä yhden pitkän työvuoron vaiko monta lyhyempää vuoroa?',
        choices=SHIFT_TYPE_CHOICES,
    )

    total_work = models.CharField(max_length=15,
        verbose_name='Toivottu kokonaistyömäärä',
        help_text='Kuinka paljon haluat tehdä töitä yhteensä tapahtuman aikana? Useimmissa tehtävistä minimi on kahdeksan tuntia, mutta joissain tehtävissä se voi olla myös vähemmän (esim. majoitusvalvonta 6 h).',
        choices=TOTAL_WORK_CHOICES,
    )

    overseer = models.BooleanField(
        default=False,
        verbose_name='Olen kiinnostunut vuorovastaavan tehtävistä',
        help_text='Vuorovastaavat ovat kokeneempia conityöläisiä, jotka toimivat oman tehtäväalueensa tiiminvetäjänä.',
    )

    want_certificate = models.BooleanField(
        default=False,
        verbose_name='Haluan todistuksen työskentelystäni Traconissa',
    )

    certificate_delivery_address = models.TextField(
        blank=True,
        verbose_name='Työtodistuksen toimitusosoite',
        help_text='Jos haluat työtodistuksen, täytä tähän kenttään postiosoite (katuosoite, '
            'postinumero ja postitoimipaikka) johon haluat todistuksen toimitettavan.',
    )

    shirt_size = models.CharField(
        max_length=8,
        choices=SHIRT_SIZES,
        verbose_name='Paidan koko',
        help_text='Ajoissa ilmoittautuneet vänkärit saavat maksuttoman työvoimapaidan. '
            'Kokotaulukot: <a href="http://www.bc-collection.eu/uploads/sizes/TU004.jpg" '
            'target="_blank">unisex-paita</a>, <a href="http://www.bc-collection.eu/uploads/sizes/TW040.jpg" '
            'target="_blank">ladyfit-paita</a>',
    )

    special_diet = models.ManyToManyField(
        SpecialDiet,
        blank=True,
        verbose_name='Erikoisruokavalio'
    )

    special_diet_other = models.TextField(
        blank=True,
        verbose_name='Muu erikoisruokavalio',
        help_text='Jos noudatat erikoisruokavaliota, jota ei ole yllä olevassa listassa, '
            'ilmoita se tässä. Tapahtuman järjestäjä pyrkii ottamaan erikoisruokavaliot '
            'huomioon, mutta kaikkia erikoisruokavalioita ei välttämättä pystytä järjestämään.'
    )

    lodging_needs = models.ManyToManyField(Night,
        blank=True,
        verbose_name='Tarvitsen lattiamajoitusta',
        help_text='Ruksaa ne yöt, joille tarvitset lattiamajoitusta. Lattiamajoitus sijaitsee '
            'kävelymatkan päässä tapahtumapaikalta.',
    )

    prior_experience = models.TextField(
        blank=True,
        verbose_name='Työkokemus',
        help_text='Kerro tässä kentässä, jos sinulla on aiempaa kokemusta vastaavista '
            'tehtävistä tai muuta sellaista työkokemusta, josta arvioit olevan hyötyä '
            'hakemassasi tehtävässä.'
    )

    free_text = models.TextField(
        blank=True,
        verbose_name='Vapaa alue',
        help_text='Jos haluat sanoa hakemuksesi käsittelijöille jotain sellaista, jolle ei ole '
            'omaa kenttää yllä, käytä tätä kenttää.'
    )

    email_alias = models.CharField(
        blank=True,
        default='',
        max_length=32,
        verbose_name='Sähköpostialias',
        help_text='Coniitit saavat käyttöönsä nick@tracon.fi-tyyppisen sähköpostialiaksen, joka '
            'ohjataan coniitin omaan sähköpostilaatikkoon. Tässä voit toivoa haluamaasi sähköpostialiaksen alkuosaa eli sitä, joka tulee ennen @tracon.fi:tä. '
            'Sallittuja merkkejä ovat pienet kirjaimet a-z, numerot 0-9 sekä väliviiva.',
        validators=[validate_slug]
    )

    @classmethod
    def get_form_class(cls):
        from .forms import SignupExtraForm
        return SignupExtraForm

    @staticmethod
    def get_query_class():
        return SignupX

    @property
    def formatted_lodging_needs(self):
        return "\n".join("{night}: {need}".format(
            night=night.name,
            need='Tarvitsee lattiamajoitusta' if self.lodging_needs.filter(pk=night.pk).exists() else 'Ei tarvetta lattiamajoitukselle',
        ) for night in Night.objects.all())


class SignupX(QueryBuilder):
    model = SignupExtra
    query_related_exclude = {
        "signup": ("event",),
    }
    query_related_filter = {
        "signup": "*",
        "signup__person": ("birth_date",),
    }
    view_related_filter = {
        "signup__person": ("first_name", "surname", "nick", "birth_date", "email", "phone",),
    }
    default_views = [
        "signup__person__first_name",
        "signup__person__surname",
        "signup__person__nick",
    ]
    view_groups = (
        ("Henkilötiedot", add_prefix("signup__person__", (
            "surname", "first_name", "nick", "phone", "email", "birth_date"))),
        ("Sisäiset", add_prefix("signup__", (
            "state", "job_categories_accepted__pk", "notes", "created_at", "updated_at"))),
        ("Työvuorotoiveet", "signup__job_categories__pk", "shift_type", "total_work", "overseer"),
        ("Työtodistus", "want_certificate", "certificate_delivery_address"),
        ("Lisätiedot", "shirt_size", "special_diet__pk", "special_diet_other",
            "lodging_needs__pk", "prior_experience", "free_text"),
        ("Tila", add_prefix("signup__time_", ("accepted", "finished", "complained", "cancelled",
                                              "rejected", "arrived", "work_accepted", "reprimanded",))),
    )
