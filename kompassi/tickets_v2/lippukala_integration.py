# https://docs.google.com/spreadsheet/ccc?key=0Annwjrq9JeBldGQ3aEFRakpJeGtISUVpTnpJRl92dUE&usp=drive_web#gid=0
KEYSPACE = list(
    set(
        """
ahma    arkki   ääni    höyry   kulta   aita    piano   hylly   hame    kahvi   viiva
ahven   hihna   aika    ilma    kumi    muuri   rumpu   kuori   huppu   maito   kaari
eläin   johto   aste    päivä   lanka   talo    torvi   kynä    kenkä   liha    käyrä
hauki   kirja   avain   pilvi   muovi   torni   viulu   mappi   mekko   kaali   suora
    kivi    jakso   pouta   nahka   kokko   sello   tasku   paita   jauho   pallo
hylje   lakki   jalka   sade    naru    salko       vihko   sukka   riisi   pinta
ilves   lappu   kanta   sähkö   pahvi   maja        kirje       hillo   taso
kettu   lasi    katu    tuuli   rauta   katos                  jana
karhu   lehti   kausi   valo    teräs                   puuro   piste
    levy    kesto   aalto   hiili
kala    mitta   kone        rikki
    nauha   kuva        tina
kotka   noppa   laulu
kuha    nuoli   lause
lahna   pannu   lento
näätä   pullo   lista
närhi       meemi
rotta       melu
varis       mieli
heppa       muoto
siika       pohja
        posti
        raha
        raita
        sana
        taide
        vaara
        väri
        vesi
        viesti
        vuosi
        ihme
        voima
        hissi
""".split()
    )
)


class Queue:
    ONE_QUEUE = "1"


PREFIXES = {
    Queue.ONE_QUEUE: "kissa",
}

KEYSPACES = {
    Queue.ONE_QUEUE: KEYSPACE,
}


def select_queue(_):
    return Queue.ONE_QUEUE
