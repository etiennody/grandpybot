import pytest
import requests

from app.maps import Maps


def test_get_maps_information_for_openclassrooms(monkeypatch):

    address = {
        "formatted_address": "7 Cité Paradis, 75010 Paris, France",
        "lat": "48.8748465",
        "lng": "2.3504873",
    }

    class MockRequestsGet:
        def __init__(self, url, params=None):
            pass

        def json(self):
            return {
                "results": [
                    {
                        "formatted_address": address["formatted_address"],
                        "geometry": {
                            "location": {"lat": address["lat"], "lng": address["lng"]}
                        },
                    }
                ]
            }

    monkeypatch.setattr("requests.get", MockRequestsGet)

    assert Maps().get_maps_information("openclassrooms") == address
