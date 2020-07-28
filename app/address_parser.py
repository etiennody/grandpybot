import re
import string

from app.constant import PATTERN_REGEX_PARSER


class AddressMatchNotFound(Exception):
    """Processing a custom error.

    Args:
        Exception (string): a sentence when an error is detected.
    """

    pass


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
    pattern = PATTERN_REGEX_PARSER
    response = None
    for p in pattern:
        response = re.search(p, message)
        if response:
            break
    if not response:
        raise AddressMatchNotFound("Ooops, not match found")
    return response.group(1).strip()
