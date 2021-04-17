"""
this module contains the pokedex class.
"""
import errno
import multiprocessing
import sys

import args
from exceptions import InvalidObjectException
from pokeapigetter import PokeApiGetter
from pokedexrequest import Request
from report import Report


class PokeDex:
    """
    Represents a pokedex, Drives the program.
    """
    def __init__(self):
        """
        Constructor.
        """
        self.pokedex_objects = None
        self.arguments = None

    def get_poke_list(self):
        """
        Return a list of pokemon names from file.
        :return: a list of pokemon names from file.
        """
        if self.arguments.input_file is None:
            poke_list = [self.arguments.input_data]

        else:
            try:
                poke_list = self.get_pokemon_in_file(self.arguments.input_file)
            except IOError as error:
                if error.errno == errno.EACCES:
                    print("Cannot read data from file")

                elif error.errno == errno.ENOENT:
                    print("File not found")
                sys.exit(1)
        return poke_list

    def execute_report(self):
        """
        Formats the report.
        """
        if self.arguments.output_file is None:
            Report.console_report(self.pokedex_objects)

        else:
            Report.file_output_report(self.pokedex_objects, self.arguments.output_file)

    def start(self):
        """
        Starts the program.
        :return: none.
        """
        self.arguments = args.ArgumentParser.set_parser()

        poke_list = self.get_poke_list()

        requests = []

        for item in poke_list:
            requests.append(Request(self.arguments.mode, item, self.arguments.expanded, 4))

        api_call = PokeApiGetter(requests, multiprocessing.cpu_count())

        try:
            self.pokedex_objects = api_call.get_api()
        except InvalidObjectException as e:
            print(e)
            sys.exit(2)

        self.execute_report()

    @staticmethod
    def get_pokemon_in_file(file_name) -> list:
        with open(file_name, mode='r', encoding='utf-8') as file:
            return [line.strip('\n') for line in file]


def main():
    """
    Main function.
    """
    driver = PokeDex()
    driver.start()


if __name__ == '__main__':
    main()
