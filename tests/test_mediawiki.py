import pytest
import requests

from app.mediawiki import MediaWiki


def test_get_mediawiki_information_for_le_quartz(monkeypatch):

    wiki_extract = (
        "Le Quartz est créé en 1988 à la suite de l'incendie qui détruit complètement "
        "le Palais des Arts et de la Culture le 26 novembre 1981. La reconstruction voit le jour "
        "sous l'ère de Georges Kerbrat, maire de Brest, après que Jacques Berthelot, élu maire en 1983, "
        "décida de conserver comme socle les parties épargnées par l'incendie, "
        "notamment le long de l'avenue Clemenceau."
    )

    class MockRequestsGet:
        def __init__(self, url, params=None):
            pass

        def json(self):
            return {"query": {"pages": {"key": {"extract": wiki_extract}}}}

    monkeypatch.setattr("requests.get", MockRequestsGet)

    assert MediaWiki().get_mediawiki_information("48.3856", "-4.4853") == wiki_extract
