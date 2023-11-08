import random
import string
from .models import RawVerses


class RandWord:
    @classmethod
    def get_html_name_verse(cls):
        html_name_verse = RawVerses.objects.all().values_list("html_name", "verses")
        return html_name_verse

    @classmethod
    def split_str_words(cls, list_str_words):
        list_split_words_punc = [
            long_str.translate(
                str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~...–…")
            ).split()
            for long_str in list_str_words
        ]
        return list_split_words_punc

    @classmethod
    def make_list_html_name_rand_word(cls):
        html_name_verse = cls.get_html_name_verse()
        html_name_rand_word = []
        for t_v in html_name_verse:
            html_name = t_v[0]
            verse_as_split_words = cls.split_str_words([t_v[1]])[0]
            rand_number = random.randint(0, len(verse_as_split_words) - 1)
            rand_word = verse_as_split_words[rand_number]
            rand_word = rand_word.lower()
            html_name_rand_word.append([html_name, rand_word])
        return html_name_rand_word
