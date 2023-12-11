import random
from .models import RawVerses, EuPro


class RandWord:
    @classmethod
    def get_html_name_verse(cls):
        queryset = RawVerses.objects.all().order_by("-date_of_writing")
        html_name_verse = queryset.values_list("html_name", "verses")
        return html_name_verse

    @classmethod
    def get_html_name_fact(cls):
        queryset = EuPro.objects.all().order_by("-date_of_writing")
        html_name_fact = queryset.values_list("html_name", "fact")
        return html_name_fact

    @classmethod
    def split_str_words(cls, list_str_words):
        signs_to_rm = "!\"#$%&'()*+,./:;<=>?@[\\]^_`{|}~...–…"
        translation_table = str.maketrans("", "", signs_to_rm)
        list_split_words_punc = []
        for long_str in list_str_words:
            split_str = long_str.translate(translation_table).split()
            list_split_words_punc.append(split_str)

        return list_split_words_punc

    @classmethod
    def make_list_html_name_rand_word(cls, html_name_text):
        html_name_rand_word = []
        for t_v in html_name_text:
            html_name = t_v[0]
            verse_as_split_words = cls.split_str_words([t_v[1]])[0]

            while True:
                rand_number = random.randint(0, len(verse_as_split_words) - 1)
                rand_word = verse_as_split_words[rand_number]
                rand_word = rand_word.lower()
                if rand_word != "-":
                    break

            html_name_rand_word.append([html_name, rand_word])

        return html_name_rand_word

    @classmethod
    def get_verse_html_name_rand_word(cls):
        text = cls.get_html_name_verse()
        verse_html_name_rand_word = cls.make_list_html_name_rand_word(text)
        return verse_html_name_rand_word

    @classmethod
    def get_fact_html_name_rand_word(cls):
        text = cls.get_html_name_fact()
        fact_html_name_rand_word = cls.make_list_html_name_rand_word(text)
        return fact_html_name_rand_word
