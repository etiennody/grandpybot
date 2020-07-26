import re
import string


class AddressMatchNotFound(Exception):
    """Processing a custom error.

    Args:
        Exception (string): a sentence when an error is detected.
    """
    pass


class Parser:
    """Cutting a set of data into small, separately manipulable sets.
    """

    @staticmethod
    def address_parser(message):
        """
        Use Regex to parse input of user and
        retain interesting key words.

        Args:
            message (string): the input of user.

        Raises:
            AddressMatchNotFound: processing a custom error.

        Returns:
            string: key words retain to processs in app.
        """

        message = message.lower()
        pattern = [
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
        response = None
        for p in pattern:
            response = re.search(p, message)
            if response:
                break
        if not response:
            raise AddressMatchNotFound("Ooops, not match found")
        return response.group(1).strip()
