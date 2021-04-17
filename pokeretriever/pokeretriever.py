"""
This module contains the pokedex object and its concrete implementations.
"""


class PokedexObject:
    """
    Represents a pokedex object.
    """

    def __init__(self, name: str, id: int):
        """
        Constructor.
        :param name: Name of pokemon.
        :param id: ID of entry.
        """
        self.name = name
        self.id = id

    def __str__(self):
        """
        String representation of instance.
        :return: a string.
        """
        return f'PokedexObject={str(vars(self))}'


class Pokemon(PokedexObject):
    """
    Class that stores a pokemon's information.
    """

    def __init__(self, name: str, id: int, height: int, weight: int, stats,
                 types: list, abilities, move, expanded: bool):
        """
        Constructor.

        :param height: int: the height of the Pokemon
        :param weight: int: the weight of the Pokemon
        :param stats: the pokemon's stats
        :param types: request_type request_type for pokemon
        :param abilities: the pokemon's abilities
        :param move: the pokemon's moves
        """
        super().__init__(name, id)
        self.height = height
        self.weight = weight
        self.stats = stats
        self.types = types
        self.abilities = abilities
        self.move = move
        self.expanded = expanded

    def ability_str(self):
        """
        Return a string representation of the pokemon's abilities.
        :return: a String.
        """
        result = ''

        for ability in self.abilities:
            if self.expanded:
                ability = str(ability).replace('\n', "\n\t\t")
                result += f'{ability}'
            else:
                result += f'\n\t\t{ability}'

        return result

    def type_str(self):
        """
        Return a string representation of the pokemon's mode.
        :return: a String.
        """
        result = ''
        for a_type in self.types:
            result += f'\n\t\t Name: {a_type}'
        return result

    def move_str(self):
        """
        Return a string representation of the pokemon's moves.
        :return: a String.
        """
        result = ''
        if self.expanded:
            for move in self.move:
                move = str(move).replace('\n', "\n\t\t")
                result += f'\n\t\t{move}'
            return result
        else:
            result = ''
            for move in self.move:
                result += f'\n\t\t(Move name: {move[0]}, Level acquired: {move[1]})'
            return result

    def stat_str(self):
        """
        Return a string representation of the pokemon's stats.
        :return: a String.
        """
        result = ''
        if self.expanded:
            for stat in self.stats:
                stat = str(stat).replace('\n', "\n\t\t")
                result += f'\n\t\t{stat}'
            return result

    def __str__(self):
        """Returns the current Pokemon's details"""
        return f'Pokemon: {self.name} ' \
               f'\n\tID: {self.id}' \
               f'\n\tHeight: {self.height}' \
               f'\n\tWeight: {self.weight}' \
               f'\n\tTypes: {self.type_str()}' \
               f'\n\tStats: {self.stat_str()}' \
               f'\n\t--------- ' \
               f'\n\tAbilities: {self.ability_str()}' \
               f'\n\tMoves: {self.move_str()}' \
               f'\n\tExpanded: {self.expanded}'


class Ability(PokedexObject):
    """
    Class that stores the information of an ability.
    """

    def __init__(self, name: str, id: int, generation: str, effect: str,
                 effect_short: str, pokemon: list):
        """
        Constructor.

        :param name: str : name of the ability
        :param id: int: id of the ability
        :param generation: generation the ability was made
        :param effect: effect's ability
        :param effect_short: short description of effect
        :param pokemon: list of pokemon with this ability

        """
        super().__init__(name, id)
        self.generation = generation
        self.effect = effect
        self.effect_short = effect_short
        self.pokemon = pokemon

    def __str__(self):
        """
        Return string representation of this instance.
        :return: a String.
        """
        effect = self.effect.replace("\n", " ")
        effect_short = self.effect_short.replace('\n', ' ')
        result = f'\nName: {self.name}' \
                 f'\nId: {self.id}' \
                 f'\nGeneration: {self.generation}' \
                 f'\nEffect: {effect}, ' \
                 f'\nEffect short: {effect_short}' \
                 f'\nPokemon:'
        for pokemon in self.pokemon:
            result += f' {pokemon}'
        return result


class Move(PokedexObject):
    """
    Stores the information about a move a pokemon can do (attacks/ actions).
    """

    def __init__(self, name: str, id: int, generation: str, accuracy: int,
                 powerpoints: int, power: int, type: str, damage_class: str,
                 effect_short: str):
        """
        Constructor.

        :param generation: string: generation move was created in
        :param accuracy: how accurate a pokemons move is
        :param powerpoints: int: number of times move can be used
        :param power: original power of the move
        :param type: request_type of move
        :param damage_class: damage class
        :param effect_short: description of pokemons effect
        """
        super().__init__(name, id)
        self.generation = generation
        self.accuracy = accuracy
        self.powerpoints = powerpoints
        self.power = power
        self.type = type
        self.damage_class = damage_class
        self.effect_short = effect_short

    def __str__(self):
        """Returns the current state of the Move"""
        return f'\nName: {self.name}' \
               f'\nId: {self.id}' \
               f'\nGeneration: {self.generation}' \
               f'\nAccuracy: {self.accuracy}' \
               f'\npowerpoints: {self.powerpoints}' \
               f'\nPower: {self.power}' \
               f'\nType: {self.type}' \
               f'\nMove Damage Class: {self.damage_class}' \
               f'\nEffect (Short): {self.effect_short}'


class Stat(PokedexObject):
    """
    Class that contains the stats of the pokemon.
    """

    def __init__(self, name: str, id: int, is_battle_only: bool):
        """
        :param is_battle_only: if the pokemon is battle only
        """
        super().__init__(name, id)
        self.is_battle_only = is_battle_only

    def __str__(self):
        """
        Return the string representation of this instance.
        :return: a String.
        """
        return f'\nName: {self.name}' \
               f'\nID: {self.id}' \
               f'\nIs_Battle_Only: {self.is_battle_only}'
