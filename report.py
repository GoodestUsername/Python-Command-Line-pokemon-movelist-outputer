"""
Module containing class to output the report.
"""

from datetime import datetime


class Report:
    """
    Contains methods that to output results.
    """
    @staticmethod
    def file_output_report(pokedexobject_list: list, file_name: str):
        """
        Output report to file.

        :param file_name: path of file
        :param pokedexobject_list:list of PokedexObjects.
        """

        with open(file_name, 'w') as file:
            file.write('Timestamp: ' + str(datetime.now()) + '\n')
            for pokedexobject in pokedexobject_list:
                file.write(str(pokedexobject))

    @staticmethod
    def console_report(pokedexobject_list: list):
        """
        Print the report.

        :param pokedexobject_list: list of PokedexObjects.
        """
        print('Console Report')
        for pokedexobject in pokedexobject_list:
            print(pokedexobject)
