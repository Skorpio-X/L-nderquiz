from functools import partial

from . import globs as gl
from .game_class import Game
from .flagquiz import FlagQuiz
from .titlemenu import (TitleMain, TitleCountries, TitleCapitals, TitleFlags,
                        Options)
from .lists import (AUSTRALIAOCEANIA_LIST, SOUTHAMERICA_LIST, ASIA_LIST,
                    NORTHAMERICA_LIST, EUROPE_LIST, AFRICA_LIST)


scenes = {
    'TitleMain': TitleMain,
    'TitleCountries': TitleCountries,
    'TitleCapitals': TitleCapitals,
    'TitleFlags': TitleFlags,
    'Options': Options,
    'Europe':
        partial(Game, gl.EUROPE_MAP, EUROPE_LIST, 1, 'Africa'),
    'Africa':
        partial(Game, gl.AFRICA_MAP, AFRICA_LIST, 1, 'Asia'),
    'Asia':
        partial(Game, gl.ASIA_MAP, ASIA_LIST, 1, 'SouthAmerica'),
    'SouthAmerica':
        partial(Game, gl.SOUTHAMERICA_MAP, SOUTHAMERICA_LIST, 1,
                'NorthAmerica'),
    'NorthAmerica':
        partial(Game, gl.NORTHAMERICA_MAP, NORTHAMERICA_LIST, 1,
                'AustraliaOceania'),
    'AustraliaOceania':
        partial(Game, gl.AUSTRALIAOCEANIA_MAP, AUSTRALIAOCEANIA_LIST, 1,
                'Europe'),
    'EuropeCountries':
        partial(Game, gl.EUROPE_MAP, EUROPE_LIST, 2, 'AfricaCountries'),
    'AfricaCountries':
        partial(Game, gl.AFRICA_MAP2, AFRICA_LIST, 2, 'AsiaCountries'),
    'AsiaCountries':
        partial(Game, gl.ASIA_MAP2, ASIA_LIST, 2, 'SouthAmericaCountries'),
    'SouthAmericaCountries':
        partial(Game, gl.SOUTHAMERICA_MAP2, SOUTHAMERICA_LIST, 2,
                'NorthAmericaCountries'),
    'NorthAmericaCountries':
        partial(Game, gl.NORTHAMERICA_MAP2, NORTHAMERICA_LIST, 2,
                'AustraliaOceaniaCountries'),
    'AustraliaOceaniaCountries':
        partial(Game, gl.AUSTRALIAOCEANIA_MAP2, AUSTRALIAOCEANIA_LIST, 2,
                'EuropeCountries'),
    'EuropeFlags':
        partial(FlagQuiz, gl.FLAGS_EUROPE, EUROPE_LIST, 'AfricaFlags'),
    'AfricaFlags':
        partial(FlagQuiz, gl.FLAGS_AFRICA, AFRICA_LIST, 'AsiaFlags'),
    'AsiaFlags':
        partial(FlagQuiz, gl.FLAGS_ASIA, ASIA_LIST, 'SouthAmericaFlags'),
    'SouthAmericaFlags':
        partial(FlagQuiz, gl.FLAGS_SOUTHAMERICA, SOUTHAMERICA_LIST, 'NorthAmericaFlags'),
    'NorthAmericaFlags':
        partial(FlagQuiz, gl.FLAGS_NORTHAMERICA, NORTHAMERICA_LIST, 'AustraliaOceaniaFlags'),
    'AustraliaOceaniaFlags':
        partial(FlagQuiz, gl.FLAGS_AUSTRALIAOCEANIA, AUSTRALIAOCEANIA_LIST, 'EuropeFlags'),
    }
