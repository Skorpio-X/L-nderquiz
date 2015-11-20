"""List of european countries with corresponding capitals."""
# from operator import itemgetter
# from ..globs import flags_euro
# from ..globs import _


EUROPE_LIST = [
    [(377, 489), _('Tirana'), _('Albanien'), 'Albania'],
    [(164, 457), _('Andorra la Vella'), _('Andorra'), 'Andorra'],
    [(215, 336), _('Brüssel'), _('Belgien'), 'Belgium'],
    [(355, 448), _('Sarajevo'), _('Bosnien und Herzegowina'), 'Bosnia_and_Herzegovina'],
    [(415, 461), _('Sofia'), _('Bulgarien'), 'Bulgaria'],
    [(303, 314), _('Berlin'), _('Deutschland'), 'Germany'],
    [(296, 268), _('Kopenhagen'), _('Dänemark'), 'Denmark'],
    [(398, 205), _('Tallinn'), _('Estland'), 'Estonia'],
    [(394, 191), _('Helsinki'), _('Finnland'), 'Finland'],
    [(189, 364), _('Paris'), _('Frankreich'), 'France'],
    [(428, 535), _('Athen'), _('Griechenland'), 'Greece'],
    [(123, 274), _('Dublin'), _('Irland'), 'Ireland'],
    [( 72,  74), _('Reykjavik'), _('Island'), 'Iceland'],
    [(295, 485), _('Rom'), _('Italien'), 'Italy'],
    [(328, 420), _('Zagreb'), _('Kroatien'), 'Croatia'],
    [(394, 243), _('Riga'), _('Lettland'), 'Latvia'],
    [(262, 397), _('Vaduz'), _('Liechtenstein'), 'Liechtenstein'],
    [(410, 278), _('Vilnius'), _('Litauen'), 'Lithuania'],
    [(229, 354), _('Luxemburg'), _('Luxemburg'), 'Luxembourg'],
    [(311, 575), _('Valetta'), _('Malta'), 'Malta'],
    [(394, 475), _('Skopje'), _('Mazedonien'), 'Macedonia'],
    [(463, 389), _('Chisinau'), _('Moldawien'), 'Moldova'],
    [(227, 447), _('Monaco'), _('Monaco'), 'Monaco'],
    [(366, 472), _('Podgorica'), _('Montenegro'), 'Montenegro'],
    [(223, 311), _('Amsterdam'), _('Niederlande'), 'Netherlands'],
    [(284, 200), _('Oslo'), _('Norwegen'), 'Norway'],
    [(332, 384), _('Wien'), _('Österreich'), 'Austria'],
    [(373, 319), _('Warschau'), _('Polen'), 'Poland'],
    [( 26, 481), _('Lissabon'), _('Portugal'), 'Portugal'],
    [(444, 429), _('Bukarest'), _('Rumänien'), 'Romania'],
    [(506, 236), _('Moskau'), _('Russland'), 'Russia'],
    [(289, 450), _('San Marino'), _('San Marino'), 'San_Marino'],
    [(343, 210), _('Stockholm'), _('Schweden'), 'Sweden'],
    [(239, 399), _('Bern'), _('Schweiz'), 'Switzerland'],
    [(377, 442), _('Belgrad'), _('Serbien'), 'Serbia'],
    [(342, 383), _('Bratislava'), _('Slowakei'), 'Slovakia'],
    [(314, 416), _('Ljubljana'), _('Slowenien'), 'Slovenia'],
    [( 89, 474), _('Madrid'), _('Spanien'), 'Spain'],
    [(309, 352), _('Prag'), _('Tschechien'), 'Czech_Republic'],
    [(530, 483), _('Ankara'), _('Türkei'), 'Turkey'],
    [(470, 334), _('Kiew'), _('Ukraine'), 'Ukraine'],
    [(360, 393), _('Budapest'), _('Ungarn'), 'Hungary'],
    [(289, 480), _('Vatikanstadt'), _('Vatikanstadt'), 'Vatican_City'],
    [(176, 318), _('London'), _('Vereinigtes Königreich'), 'United_Kingdom'],
    [(429, 285), _('Minsk'), _('Weißrussland'), 'Belarus'],
    [(557, 557), _('Nikosia'), _('Zypern'), 'Cyprus'],
    ]

# sorted_list = sorted(EUROPE_LIST, key=itemgetter(2))
# print(sorted_list)
# sorted_flags = [name for name in sorted(flags_euro)]
# for (pos, capital, country), country_engl in zip(sorted_list, sorted_flags):
#     print("[{0}, '{1}', '{2}', '{3}'],".format(pos, capital, country, country_engl))
