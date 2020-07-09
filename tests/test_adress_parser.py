import pytest

from app.address_parser import Parser


def test_parser_ok():
    """
    Test the entire method.
    Choose different cases.
    """
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
    Have to return the last words of the sentence.
    """
    text = "Bonjour, savez-vous où se situe la Tour Eiffel ?"
    address = Parser.address_parser(text)
    assert address == "tour eiffel"


def test_parser_without_stop_words():
    """
    Test if the french stop words treatment doesn't get out the parser method.
    """
    text = "Ordinateurs soutiennent utilisateur"
    address = Parser.address_parser(text)
    assert address == "ordinateurs soutiennent utilisateur"


def test_parser_str_lower():
    """
    Test if lower case have changed the parsing word retained.
    """
    text = "Je veux aller à Brest"
    address = Parser.address_parser(text)
    assert address == "brest"


def test_parser_return_str():
    """
    Test if the address contains some punctuations only.
    """
    text = "? ! , . / ="
    with pytest.raises(ValueError):
        Parser.address_parser(text)


def test_parser_send_no_value():
    """
    Test if parser is wordless.
    """
    text = ""
    with pytest.raises(ValueError):
        Parser.address_parser(text)


def test_parser_returns_no_data():
    """
    Test if parser returns any data.
    """
    text = "Bonjour !"
    with pytest.raises(ValueError):
        Parser.address_parser(text)


def test_parser_word_with_punctuation():
    """
    Test if a punctuation is pasted to the word is correctly processed.
    """
    text = "Salut, je veux découvrir Brest!"
    address = Parser.address_parser(text)
    assert address == "brest"


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
