from functools import partial

from . import globs as gl
from .game_class import Game
from .titlemenu import TitleMain, TitleCountries, TitleCapitals, Options
from .lists import (AUSTRALIAOCEANIA_LIST, SOUTHAMERICA_LIST, ASIA_LIST,
                    NORTHAMERICA_LIST, EUROPE_LIST, AFRICA_LIST)


scenes = {
    'TitleMain': TitleMain,
    'TitleCountries': TitleCountries,
    'TitleCapitals': TitleCapitals,
    'Options': Options,
    'Europe':
        partial(Game, 'Africa', gl.EUROPE_MAP, EUROPE_LIST, 1),
    'Africa':
        partial(Game, 'Asia', gl.AFRICA_MAP, AFRICA_LIST, 1),
    'Asia':
        partial(Game, 'SouthAmerica', gl.ASIA_MAP, ASIA_LIST, 1),
    'SouthAmerica':
        partial(Game, 'NorthAmerica', gl.SOUTHAMERICA_MAP,
                SOUTHAMERICA_LIST, 1),
    'NorthAmerica':
        partial(Game, 'AustraliaOceania', gl.NORTHAMERICA_MAP,
                NORTHAMERICA_LIST, 1),
    'AustraliaOceania':
        partial(Game, 'Europe', gl.AUSTRALIAOCEANIA_MAP,
                AUSTRALIAOCEANIA_LIST, 1),
    'EuropeCountries':
        partial(Game, 'AfricaCountries', gl.EUROPE_MAP, EUROPE_LIST, 2),
    'AfricaCountries':
        partial(Game, 'AsiaCountries', gl.AFRICA_MAP2, AFRICA_LIST, 2),
    'AsiaCountries':
        partial(Game, 'SouthAmericaCountries', gl.ASIA_MAP2, ASIA_LIST, 2),
    'SouthAmericaCountries':
        partial(Game, 'NorthAmericaCountries', gl.SOUTHAMERICA_MAP2,
                SOUTHAMERICA_LIST, 2),
    'NorthAmericaCountries':
        partial(Game, 'AustraliaOceaniaCountries', gl.NORTHAMERICA_MAP2,
                NORTHAMERICA_LIST, 2),
    'AustraliaOceaniaCountries':
        partial(Game, 'EuropeCountries', gl.AUSTRALIAOCEANIA_MAP2,
                AUSTRALIAOCEANIA_LIST, 2),
    }
