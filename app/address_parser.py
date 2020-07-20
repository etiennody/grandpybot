import re
import string


class Parser:
    """Cutting a set of data into small, separately manipulable sets.
    """

    @staticmethod
    def address_parser(message):

        message = message.lower()
        pattern = [
            r".*adress d\'([^\?]*)\?",
            r".*adresse de ([^\?]*)\?",
            r".*c\'est où ([^\?]*)\?",
            r".*où se trouve ([^\?]*), ?",
            r".*où se trouve ([^\?]*)\?",
            r".*se situe ([^\?]*)\?",
            r"([^\?]*) tu connais l\'adresse\?",
        ]
        response = None
        for p in pattern:
            response = re.search(p, message)
            if response:
                break
        if not response:
            raise ValueError("Ooops, not match found")
        return response.group(1).strip()
