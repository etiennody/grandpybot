import requests


class MediaWiki:
    """MediaWiki class calls MediaWiki API"""

    MEDIAWIKI_BASE_URL = "https://fr.wikipedia.org/w/api.php"

    def get_mediawiki_information(self, lat, lng):
        """Call MediaWiki API processed by maps.py.

        Args:
            lat (string): latitude for a location.
            lng (string): longitude for a location.

        Returns:
            dictionary: with extract data from coordinates.
        """

        url = (
            f"{self.MEDIAWIKI_BASE_URL}?format=json&action=query&prop=extracts&exsentences=2"
            f"&explaintext&generator=geosearch&ggsradius=100&ggscoord={lat}|{lng}&ggslimit=2"
        )

        data = requests.get(url).json()

        try:
            key = str(list(data["query"]["pages"].keys())[0])
            wiki_extract = data["query"]["pages"][key]["extract"]
            return wiki_extract
        except KeyError:
            return "Oops, cette contrée m'est encore inconnue..."
        else:
            return "Aie, je ne sais plus où j'habite..."
