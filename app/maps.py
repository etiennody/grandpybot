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

        API_KEY = os.environ["GOOGLE_GEOCODE_API_KEY"]

        url = f"{self.GEOCODE_BASE_URL}"
        payload = {
            "language": "fr",
            "region": "fr",
            "address": f"{place}",
            "key": f"{API_KEY}",
        }

        data = requests.get(url, params=payload).json()

        if data["results"]:
            return {
                "formatted_address": data["results"][0]["formatted_address"],
                "lat": data["results"][0]["geometry"]["location"]["lat"],
                "lng": data["results"][0]["geometry"]["location"]["lng"],
            }
