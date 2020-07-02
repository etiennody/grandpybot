import pytest

from app.address_parser import Parser


def test_parser_ok():
    cases = {
        "Salut où se trouve la poste?": "poste",
        "Hello où se trouve La Poste?": "poste",
        "tu connais l'adresse de La Poste?": "poste",
        "La Poste tu connais l'adresse?": "poste",
        "c'est où la poste?": "poste",
    }
    for case, val in cases.items():
        address = Parser.address_parser(case)
        assert address == val


def test_parser():
    """
    Test the entire method.
    Must return the last word of the sentence.
    """
    text = "Bonjour, savez-vous où se situe la Tour Eiffel ?"
    address = Parser.address_parser(text)
    assert address == "tour eiffel"


def test_parser_without_stop_words():
    """
    Test if the stop words treatment is not killing the main method
    """
    text = "Ordinateurs soutiennent utilisateur"
    address = Parser.address_parser(text)
    assert address == "ordinateurs soutiennent utilisateur"


def test_parser_str_lower():
    """
    Test if the address is changed to lower case
    """
    text = "Je veux aller à Paris"
    address = Parser.address_parser(text)
    assert address == "paris"


def test_parser_return_str():
    """
    Test if the address doesn't contain words
    """
    text = "! , . / ="
    with pytest.raises(ValueError):
        Parser.address_parser(text)


def test_parser_send_no_value():
    """
    Test if no address is send
    """
    text = ""
    with pytest.raises(ValueError):
        Parser.address_parser(text)


def test_parser_returns_no_data():
    """
    Test if no parser returns no data
    """
    text = "Bonjour !"
    with pytest.raises(ValueError):
        Parser.address_parser(text)


def test_parser_word_with_punctuation():
    """
    Test if word with punctation is correctly processed
    """
    text = "Salut, je veux découvrir Paris!"
    address = Parser.address_parser(text)
    assert address == "paris"



# another_cases = [
#     "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir?",
#     "Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?",
#     "Bonsoir Grandpy, j'espère que tu as passé une belle semaine.",
#     "Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie.",
# ]

# #Passe pas ds dict
# "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?":"openclassrooms",
# "tu connais l'adresse d'openclassroom?": "poste",

# #Test OK
# text = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
# address = Parser.address_parser(text)
# assert address == "openclassrooms"
