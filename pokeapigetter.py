"""
Module containing class to handle requests from api.
"""
import concurrent

import requests
import concurrent.futures

from pokedexrequest import PokedexRequest


class PokeApiGetter:
    """
    downloads poke api and maps threads based on how many you want to pass in
    """

    def __init__(self, list_of_requests: list, threads: int):
        """
        :param list_of_requests: list of requests
        :param threads: the max threads the downloader can use.
        """
        self.requests = list_of_requests
        self.max_threads = threads

    def get_api(self):
        """
        Return a list of PokedexObjects processed from each request in the list.
        :return: list of PokedexObjects.
        """
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            with requests.Session() as session:
                return list(executor.map(PokedexRequest(session).execute_request, self.requests))
