"""List of european countries with corresponding capitals."""
# from operator import itemgetter
# from ..globs import flags_euro


def _(message):  # For deferred translation.
    return message


EUROPE_LIST = [
    [(377, 489), _('Tirana'), _('Albanien')],
    [(164, 457), _('Andorra la Vella'), _('Andorra')],
    [(215, 336), _('Brüssel'), _('Belgien')],
    [(355, 448), _('Sarajevo'), _('Bosnien und Herzegowina')],
    [(415, 461), _('Sofia'), _('Bulgarien')],
    [(303, 314), _('Berlin'), _('Deutschland')],
    [(296, 268), _('Kopenhagen'), _('Dänemark')],
    [(398, 205), _('Tallinn'), _('Estland')],
    [(394, 191), _('Helsinki'), _('Finnland')],
    [(189, 364), _('Paris'), _('Frankreich')],
    [(428, 535), _('Athen'), _('Griechenland')],
    [(123, 274), _('Dublin'), _('Irland')],
    [(72, 74), _('Reykjavik'), _('Island')],
    [(295, 485), _('Rom'), _('Italien')],
    [(328, 420), _('Zagreb'), _('Kroatien')],
    [(394, 243), _('Riga'), _('Lettland')],
    [(262, 397), _('Vaduz'), _('Liechtenstein')],
    [(410, 278), _('Vilnius'), _('Litauen')],
    [(229, 354), _('Luxemburg'), _('Luxemburg')],
    [(311, 575), _('Valetta'), _('Malta')],
    [(394, 475), _('Skopje'), _('Mazedonien')],
    [(463, 389), _('Chisinau'), _('Moldawien')],
    [(227, 447), _('Monaco'), _('Monaco')],
    [(366, 472), _('Podgorica'), _('Montenegro')],
    [(223, 311), _('Amsterdam'), _('Niederlande')],
    [(284, 200), _('Oslo'), _('Norwegen')],
    [(332, 384), _('Wien'), _('Österreich')],
    [(373, 319), _('Warschau'), _('Polen')],
    [(26, 481), _('Lissabon'), _('Portugal')],
    [(444, 429), _('Bukarest'), _('Rumänien')],
    [(506, 236), _('Moskau'), _('Russland')],
    [(289, 450), _('San Marino'), _('San Marino')],
    [(343, 210), _('Stockholm'), _('Schweden')],
    [(239, 399), _('Bern'), _('Schweiz')],
    [(377, 442), _('Belgrad'), _('Serbien')],
    [(342, 383), _('Bratislava'), _('Slowakei')],
    [(314, 416), _('Ljubljana'), _('Slowenien')],
    [(89, 474), _('Madrid'), _('Spanien')],
    [(309, 352), _('Prag'), _('Tschechien')],
    [(530, 483), _('Ankara'), _('Türkei')],
    [(470, 334), _('Kiew'), _('Ukraine')],
    [(360, 393), _('Budapest'), _('Ungarn')],
    [(289, 480), _('Vatikanstadt'), _('Vatikanstadt')],
    [(176, 318), _('London'), _('Vereinigtes Königreich')],
    [(429, 285), _('Minsk'), _('Weißrussland')],
    [(557, 557), _('Nikosia'), _('Zypern')],
    [(72, 74), _('Reykjavik'), _('Island')],
    ]


del _  # For deferred translation.

# sorted_list = sorted(EUROPE_LIST, key=itemgetter(2))
# print(sorted_list)
# sorted_flags = [name for name in sorted(flags_euro)]
# for (pos, capital, country), country_engl in zip(sorted_list, sorted_flags):
#     print("[{0}, '{1}', '{2}', '{3}'],".format(pos, capital, country, country_engl))
