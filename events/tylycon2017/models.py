# encoding: utf-8

from django.db import models

from labour.models import SignupExtraBase
from labour.querybuilder import QueryBuilder, add_prefix


# NIGHT_WORK_CHOICES = [
#     (u'miel', u'Työskentelen mielelläni yövuorossa'),
#     (u'tarv', u'Voin tarvittaessa työskennellä yövuorossa'),
#     (u'ei', u'En vaan voi työskennellä yövuorossa'),
# ]

# SHIRT_SIZES = [
#     (u'NO_SHIRT', u'Ei paitaa'),

#     (u'XS', u'XS Unisex'),
#     (u'S', u'S Unisex'),
#     (u'M', u'M Unisex'),
#     (u'L', u'L Unisex'),
#     (u'XL', u'XL Unisex'),
#     (u'XXL', u'XXL Unisex'),
#     (u'3XL', u'3XL Unisex'),
#     (u'4XL', u'4XL Unisex'),
#     (u'5XL', u'5XL Unisex'),

#     (u'LF_XS', u'XS Ladyfit'),
#     (u'LF_S', u'S Ladyfit'),
#     (u'LF_M', u'M Ladyfit'),
#     (u'LF_L', u'L Ladyfit'),
#     (u'LF_XL', u'XL Ladyfit'),
# ]


SHIFT_TYPE_CHOICES = [
    ('yksipitka', 'Yksi pitkä vuoro'),
    ('montalyhytta', 'Monta lyhyempää vuoroa'),
    ('kaikkikay', 'Kumpi tahansa käy'),
]

TOTAL_WORK_CHOICES = [
    ('4h', 'Minimi - 4 tuntia'),
    ('6h', '6 tuntia'),
    ('8h', '8 tuntia'),
    ('12h', '10–12 tuntia'),
#    (u'yli12h', 'Työn Sankari! Yli 12 tuntia!'),
]


class SimpleChoice(models.Model):
    name = models.CharField(max_length=63)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class SpecialDiet(SimpleChoice):
    pass


class SignupExtra(SignupExtraBase):
    shift_type = models.CharField(max_length=15,
        verbose_name='Toivottu työvuoron pituus',
        help_text='Haluatko tehdä yhden pitkän työvuoron vaiko monta lyhyempää vuoroa?',
        choices=SHIFT_TYPE_CHOICES,
    )

    total_work = models.CharField(max_length=15,
        verbose_name='Toivottu kokonaistyömäärä',
        help_text='Kuinka paljon haluat tehdä töitä yhteensä tapahtuman aikana?',
        choices=TOTAL_WORK_CHOICES,
    )

    shift_setup = models.BooleanField(
        default=False,
        verbose_name='Voin työskennellä aamulla klo 8 alkaen',
        help_text='Ensimmäiset työtehtävät alkavat klo 8. Älä valitse tätä ruutua, jos et esimerkiksi kulkuyhteyksien vuoksi pysty saapumaan Malmitalolle klo 8:an mennessä.',
    )

    shift_cleanup = models.BooleanField(
        default=False,
        verbose_name='Voin työskennellä illalla klo 20 asti',
        help_text='Viimeiset työtehtävät jatkuvat klo 20 asti. Älä valitse tätä ruutua, jos et esimerkiksi kulkuyhteyksien vuoksi pysty jäämään Malmitalolle klo 20:en asti.',
    )

    # night_work = models.CharField(max_length=5,
    #     verbose_name=u'Voitko työskennellä yöllä?',
    #     help_text=u'Yötöitä voi olla ainoastaan lauantain ja sunnuntain välisenä yönä.',
    #     choices=NIGHT_WORK_CHOICES,
    # )

    # construction = models.BooleanField(
    #     default=False,
    #     verbose_name=u'Voin työskennellä jo perjantaina',
    #     # help_text=u'Huomaathan, että perjantain ja lauantain väliselle yölle ei ole tarjolla majoitusta.',
    # )

    want_certificate = models.BooleanField(
        default=False,
        verbose_name='Haluan todistuksen työskentelystäni Tylyconissa',
    )

    # certificate_delivery_address = models.TextField(
    #     blank=True,
    #     verbose_name=u'Työtodistuksen toimitusosoite',
    #     help_text=u'Jos haluat työtodistuksen, täytä tähän kenttään postiosoite (katuosoite, '
    #         u'postinumero ja postitoimipaikka) johon haluat todistuksen toimitettavan.',
    # )

    # shirt_size = models.CharField(
    #     max_length=8,
    #     choices=SHIRT_SIZES,
    #     verbose_name=u'Paidan koko',
    #     help_text=u'Ajoissa ilmoittautuneet vänkärit saavat maksuttoman työvoimapaidan. '
    #         u'Kokotaulukot: <a href="http://www.bc-collection.eu/uploads/sizes/TU004.jpg" '
    #         u'target="_blank">unisex-paita</a>, <a href="http://www.bc-collection.eu/uploads/sizes/TW040.jpg" '
    #         u'target="_blank">ladyfit-paita</a>',
    # )

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

    # need_lodging = models.BooleanField(
    #     default=False,
    #     verbose_name=u'Tarvitsen lattiamajoitusta lauantain ja sunnuntain väliseksi yöksi',
    # )

    prior_experience = models.TextField(
        blank=True,
        verbose_name='Työkokemus',
        help_text='Kerro tässä kentässä, jos sinulla on aiempaa kokemusta vastaavista '
            'tehtävistä tai muuta sellaista työkokemusta, josta arvioit olevan hyötyä '
            'hakemassasi tehtävässä.'
    )

    # shift_wishes = models.TextField(
    #     blank=True,
    #     verbose_name=u'Alustavat työvuorotoiveet',
    #     help_text=u'Jos tiedät nyt jo, ettet pääse paikalle johonkin tiettyyn aikaan tai haluat '
    #         u'osallistua johonkin tiettyyn ohjelmanumeroon, mainitse siitä tässä.'
    # )

    motivation = models.TextField(
        blank=True,
        verbose_name='Miksi haet Tylyconiin?',
        help_text='Kerro, miksi haluat töihin juuri tähän coniin.'
    )

    free_text = models.TextField(
        blank=True,
        verbose_name='Vapaa alue',
        help_text='Jos haluat sanoa hakemuksesi käsittelijöille jotain sellaista, jolle ei ole '
            'omaa kenttää yllä, käytä tätä kenttää.'
    )

    @classmethod
    def get_form_class(cls):
        from .forms import SignupExtraForm
        return SignupExtraForm

    @classmethod
    def get_programme_form_class(cls):
        from .forms import ProgrammeSignupExtraForm
        return ProgrammeSignupExtraForm

    @staticmethod
    def get_query_class():
        raise NotImplementedError()
