PATTERN_REGEX_PARSER = [
    r".*adresse d\'([^\?]*)\?",
    r".*adresse de ([^\?]*)\?",
    r".*adresse du ([^\?]*)\?",
    r".*c\'est où ([^\?]*)\?",
    r".*c\'est ou ([^\?]*)\?",
    r".*où se trouve ([^\?]*), ?",
    r".*où se trouve ([^\?]*)\?",
    r".*ou se trouve ([^\?]*), ?",
    r".*ou se trouve ([^\?]*)\?",
    r".*se situe ([^\?]*)\?",
    r"([^\?]*) tu connais l\'adresse\?",
]

CHOICES_SENTENCES = {
    "1": "Bien sûr mon poussin ! La voici : ",
    "2": "No problemo ! C'est cadeau : ",
    "3": "Tu trouveras ton bonheur ici : ",
    "4": "Evidemment mon commandant : ",
    "5": "Tiens, j'ai quelque chose pour toi : ",
    "6": "Il me semble bien que c'est quelque part par-là : ",
}

WIKI_CHOICES_SENTENCES = {
    "1": "Indépendamment des réalités courantes ou des espérances manifestes et grandes se présentent par là. ",
    "2": "Obligé de se mettre vivement à couvert, et même ça nous paraît bête... ",
    "3": "Seule une raison, je ne plaisante jamais, répondit le maître de poste. ",
    "4": "Ratissé, peigné, cardé ; sans y comprendre un mot. ",
    "5": "Interrogez tous les types imaginables... ",
    "6": "Né à bord d'une contrée tout au diable. ",
}

