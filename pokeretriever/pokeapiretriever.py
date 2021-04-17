"""
Module contains class that gets JSON from api.
"""
from exceptions import InvalidObjectException


class PokeApiRetriever:
    """
    Class responsible for handling getting information from url.
    """
    BASE_URL = "https://pokeapi.co/api/v2/"

    @classmethod
    def get_json_from_api(cls, instance, mode, name):
        """
        Return json from url.

        :param instance: Thread instance to use for api.
        :param mode: Mode of api, a string.
        :param name: Name of entry, a string.
        :return: Json response.
        """
        url = f"{cls.BASE_URL}/{mode}/{name}"
        with instance.get(url) as response:
            if str(response.content) == "b'Not Found'":
                raise InvalidObjectException(name)
            return response.json()
