import os
import urllib.parse

import requests


class Maps:
    """Maps class calls Google Maps API"""

    GEOCODE_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

    def get_maps_information(self, place):
        """Call Google Maps API processed by address_parser.py.

        Args:
            place (string): a string input to search a location.

        Returns:
            dictionary: with formatted address, latitude and longitude data.
        """

        place = self.encode_search(place)
        API_KEY = os.environ["GOOGLE_MAPS_API_KEY"]

        url = f"{self.GEOCODE_BASE_URL}?language=fr&address={place}&key={API_KEY}"

        data = requests.get(url).json()

        if data["results"]:
            return {
                "formatted_address": data["results"][0]["formatted_address"],
                "lat": data["results"][0]["geometry"]["location"]["lat"],
                "lng": data["results"][0]["geometry"]["location"]["lng"],
            }

    def encode_search(self, place):
        """The quote() function encodes space characters to %20
        and encode space characters to plus sign (+),
        quote_plus() provided by urllib.parse package.

        Args:
            place (string): a search place provided by parser.py.

        Returns:
            string: replace ' ' with '+', as required for quoting HTML form values.
        """
        return urllib.parse.quote_plus(place)
