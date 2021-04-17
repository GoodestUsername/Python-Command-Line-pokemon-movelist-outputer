"""
Module containing class to handle requests from api.
"""
import requests
import concurrent
import concurrent.futures

from pokedexrequest import PokedexRequest


class PokeApiGetter:
    """
    downloads poke api and maps num_threads based on how many you want to pass in
    """

    def __init__(self, list_of_requests: list, num_threads: int):
        """
        :param list_of_requests: a list of requests
        :param num_threads: Max number of threads the session can use.
        """
        self.requests = list_of_requests
        self.max_threads = num_threads

    def get_pokedexobjects_from_api(self):
        """
        Return a list of PokedexObjects processed from each request in the list.
        :return: list of PokedexObjects.
        """
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            with requests.Session() as session:
                return list(executor.map(PokedexRequest(session).execute_request, self.requests))
