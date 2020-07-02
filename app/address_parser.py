import string

from app.stopwordsfr import Stopwords

class Parser:
    """Cutting a set of data into small, separately manipulable sets.
    """

    @staticmethod
    def address_parser(text):
        text = text.lower()
        punctuation_replacer = str.maketrans(string.punctuation, ' '*len(string.punctuation))    
        text_without_punctuation = ' '.join(text.translate(punctuation_replacer).split()).strip()
        filtered_text = []
        filtered_text.extend(text_without_punctuation.split())
        response = []
        for word in filtered_text:
            if not word in Stopwords.stopwords_fr:
                response.append(word)
        if not response:
            raise ValueError("")
        return ' '.join(response)
