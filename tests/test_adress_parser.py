import pytest

from app.address_parser import Parser, AddressMatchNotFound


def test_parser_ok():
    """
    Test the entire method
    to choose different cases to valide the parser function.
    """
    cases = {
        "Salut où se trouve la poste ?": "la poste",
        "Hello où se trouve La Poste?": "la poste",
        "tu connais l'adresse de La Poste?": "la poste",
        "La Poste tu connais l'adresse?": "la poste",
        "c'est où la poste?": "la poste",
        "Bonjour, savez-vous où se situe la Tour Eiffel ?": "la tour eiffel",
        "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? "
        "Au fait, pendant que j'y pense, "
        "pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, "
        "s'il te plaît?": "le musée d'art et d'histoire de fribourg",
        "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. "
        "Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? "
        "Merci d'avance et salutations à Mamie.": "la tour eiffel",
    }
    for case, val in cases.items():
        address = Parser.address_parser(case)
        assert address == val


def test_parser_ko():
    """
    Test the entire method
    to choose different cases to discard depending on the input.
    """
    cases = ["? ! , . / =", "", "Je veux aller à Brest", "Bonjour !"]
    for case in cases:
        with pytest.raises(AddressMatchNotFound):
            Parser.address_parser(case)
