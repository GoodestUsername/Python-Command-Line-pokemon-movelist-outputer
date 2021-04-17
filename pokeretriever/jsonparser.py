"""
Module contains class to parse json into objects.
"""
import concurrent
from pokeretriever.pokeretriever import Ability, Move, Pokemon, Stat
import concurrent.futures


class JSONParser:
    """
    Class containing methods to parse json into objects.
    """
    @classmethod
    def parse_json_to_pokemon_not_extended(cls, json):
        """
        Parse json into pokemon object, without extended information.

        :param json: Json to parse.
        :return: a Pokemon object.
        """
        return Pokemon(
            name=json['name'],
            id=json['id'],
            height=json['height'],
            weight=json['weight'],
            stats=[(stat['stat']['name'], stat['base_stat']) for stat in json['stats']],
            types=[a_type['type']['name'] for a_type in json['types']],
            abilities=[ability['ability']['name'] for ability in json['abilities']],
            move=[(move['move']['name'], move['version_group_details'][0]['level_learned_at'])
                  for move in json['moves']],
            expanded=False
        )

    @classmethod
    def parse_json_to_pokemon_extended(cls, json, threads):
        """
        Parse json into pokemon object, with extended information.

        :param threads: number of num_threads available, int.
        :param json: Json to parse.
        :return: a Pokemon object.
        """
        with concurrent.futures.ThreadPoolExecutor(
                max_workers=threads) as executor:
            stats = [stat['stat']['name'] for stat in json['stats']]

            list_of_stats = list(executor.map(cls.parse_json_to_stats, stats))

            abilities = [ability['ability']['name'] for ability in json['abilities']]

            list_of_abilities = list(executor.map(cls.parse_for_abilities, abilities))

            moves = [move['move']['name'] for move in json['moves']]

            list_of_moves = list(executor.map(cls.parse_json_to_move, moves))

        return Pokemon(
            name=json['name'],
            id=json['id'],
            height=json['height'],
            weight=json['weight'],
            stats=list_of_stats,
            types=[a_type['type']['name'] for a_type in json['types']],
            abilities=list_of_abilities,
            move=list_of_moves,
            expanded=True
        )

    @classmethod
    def parse_json_to_stats(cls, json):
        """
        Parse json into stats object.

        :param json: Json to parse.
        :return: a Stats object.
        """
        return Stat(
            name=json['name'],
            id=json['id'],
            is_battle_only=json['is_battle_only']
        )

    @classmethod
    def parse_for_abilities(cls, json):
        """
        Parse json into an ability object.

        :param json: Json to parse.
        :return: an Ability object.
        """
        return Ability(
            name=json['name'],
            id=json['id'],
            generation=json['generation']['name'],
            effect=json['effect_entries'][0]['effect'],
            effect_short=json['effect_entries'][0]['short_effect'],
            pokemon=[pokemon['pokemon']['name'] for pokemon in json['pokemon']]
        )

    @classmethod
    def parse_json_to_move(cls, json):
        """
        Parse json into move object.

        :param json: Json to parse.
        :return: a Move object.
        """
        return Move(
            name=json['name'],
            id=json['id'],
            generation=json['generation']['name'],
            accuracy=json['accuracy'],
            powerpoints=json['pp'],
            power=json['power'],
            type=json['type']['name'],
            damage_class=json['damage_class']['name'],
            effect_short=json['effect_entries'][0]['short_effect']
        )
