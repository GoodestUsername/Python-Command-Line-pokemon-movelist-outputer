"""
Module contains the classes to make requests from the pokemon api.
"""

from pokeretriever.jsonparser import JSONParser
from pokeretriever.pokeapiretriever import PokeApiRetriever
from pokeretriever.pokeretriever import *


class Request:
    """
    Contains the data gathered by argparse.
    """

    def __init__(self, mode: str, identifier: str, expanded: bool,
                 threads=1):
        """
        Constructor.

        :param mode: mode the program is ran in.
        :param identifier: the name / id number of the Pokemon
        :param expanded: an option of getting more information about a pokemon.
        :param threads: max num_threads the request can use.
        """
        self.mode = mode
        self.identifier = identifier
        self.expanded = expanded
        self.threads = threads

    def __str__(self):
        """Returns the current state of the request"""
        return f'current state of Request={str(vars(self))}'


class PokedexRequest:
    """
    Represents a pokedex request.
    """
    instance = None

    def __init__(self, session):
        """
        Constructor.

        :param session: Current session.
        """
        PokedexRequest.instance = session

    @classmethod
    def execute_request(cls, request: Request) -> PokedexObject:
        """
        Creates a concrete inheritor of PokedexObject from request.

        :param request: a PokedexObject
        :return: a PokedexObject
        """
        mode = request.mode
        if mode == 'pokemon':
            return cls.get_pokemon(cls.instance, mode, request.identifier, request.expanded, request.threads)
        elif mode == 'stat':
            return cls.get_stats(cls.instance, mode, request.identifier)
        elif mode == 'ability':
            return cls.get_ability(cls.instance, mode, request.identifier)
        elif mode == 'move':
            return cls.get_move(cls.instance, mode, request.identifier)

    @classmethod
    def get_pokemon(cls, instance, mode: str, name: str, expanded=False, threads=1):
        """
        Gets the pokemon from api by name.

        :param mode: Mode the program is ran in.
        :param instance: The thread instance.
        :param name: name / id of the pokemon
        :param expanded: if expanded info is requested
        :param threads: max number of num_threads allowed
        :return: a Pokemon object.
        """
        json = PokeApiRetriever.get_json_from_api(instance, mode, name)
        if expanded:
            return JSONParser.parse_json_to_pokemon_extended(json, threads)
        else:
            return JSONParser.parse_json_to_pokemon_not_extended(json)

    @classmethod
    def get_stats(cls, instance, mode: str, name: str):
        """
        Gets the stats from api by name.

        :param mode: Mode the program is ran in.
        :param instance: The thread instance.
        :param name: name / id of the stats
        :return: a Stats object.
        """
        json = PokeApiRetriever.get_json_from_api(instance, mode, name)
        return JSONParser.parse_json_to_stats(json)

    @classmethod
    def get_ability(cls, instance, mode: str, name: str):
        """
        Gets the ability from api by name.

        :param mode: Mode the program is ran in.
        :param instance: The thread instance.
        :param name: name / id of the ability
        :return: an Ability object.
        """
        json = PokeApiRetriever.get_json_from_api(instance, mode, name)
        return JSONParser.parse_for_abilities(json)

    @classmethod
    def get_move(cls, instance, mode: str, name: str):
        """
        :param mode: Mode the program is ran in.
        :param instance: The thread instance.
        :param name: name / id of the move
        :return: Move
        """
        json = PokeApiRetriever.get_json_from_api(instance, mode, name)
        return JSONParser.parse_json_to_move(json)
