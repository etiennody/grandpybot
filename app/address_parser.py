import string
import re

from app.stopwordsfr import Stopwords


class Parser:
    """Cutting a set of data into small, separately manipulable sets.
    """

    @staticmethod
    def address_parser(message):
        message = message.lower()
        punctuation_replacer = str.maketrans(
            string.punctuation, " " * len(string.punctuation)
        )
        message_without_punctuation = " ".join(
            message.translate(punctuation_replacer).split()
        ).strip()
        filtered_message = []
        filtered_message.extend(message_without_punctuation.split())
        response = []

        for word in filtered_message:
            if not word in Stopwords.stopwords_fr:
                response.append(word)
        if not response:
            raise ValueError("")
        return " ".join(response)
        
        
        # message = message.lower()
        # pattern = [
        #     r"[\s\S]*(?:(d\'|de )([^\"]*)), +",
        #     r"[\s\S]*(?:(d\'|de )([^\"]*)) +",
        #     r"[\s\S]*(?:(d\'|de )([^\"]*))+",
        #     r"[\s\S]*(?:(situe )([^\"]*)) +",
        #     r"[\s\S]*(?:(trouve )([^\"]*)) +",
        #     r"[\s\S]*(?:(est )([^\"]*)) +",
        #     r"[\s\S]*(?:(à )([^\"]*)) +",
        #     r"[\s\S]*(?:(découvrir )([^\"]*)) +",
        # ]
        # for p in pattern:
        #     response = re.search(p, message)
        #     if response:
        #         return response.group(2)
        #     else:
        #         None
        # if not response:
        #     raise ValueError("")
        # print(x.group())

# regex = r"[\s\S]*(?:(d\'|de )([^\"]*)), +
# regex_code_postale_fr = \b[0-9]{5}\b
# ^\d+\s[A-z]+\s[A-z]+