import random

from app.constant import CHOICES_SENTENCES, WIKI_CHOICES_SENTENCES


class Sentences:
    """
    List the sentences and choose twice
    for address reply and for wiki reply.
    """

    choices = CHOICES_SENTENCES
    wiki_choices = WIKI_CHOICES_SENTENCES

    @staticmethod
    def get_sentences():
        """Obtain a sentence from a random list of sentences.

        Returns:
            list: sentences for address reply and for wiki reply.
        """
        ref = str(random.randint(1, 6))
        return Sentences.choices[ref], Sentences.wiki_choices[ref]
