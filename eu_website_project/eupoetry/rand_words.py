import sqlite3
import random
import string
from pathlib import Path


# connect to db and get a verse from the main db
def connect_to_dbsqlite3():
    path_db = Path.cwd() / "verses.sqlite3"
    connect = sqlite3.connect(path_db)
    cur = connect.cursor()
    return cur


def get_list_ids():
    cur = connect_to_dbsqlite3()
    quiry_id = "SELECT id FROM raw_verses"
    list_ids = cur.execute(quiry_id).fetchall()
    list_ids = [i_d[0] for i_d in list_ids]
    cur.close()
    return list_ids


list_ids = get_list_ids()


def get_list_str_words(list_ids):
    cur = connect_to_dbsqlite3()
    list_str_words = []
    for i_d in list_ids:
        str_words = cur.execute(
            "SELECT verses FROM raw_verses WHERE id={}".format(i_d)
        ).fetchall()[0][0]
        list_str_words.append(str_words.lower())
    cur.close()
    return list_str_words


list_str_words = get_list_str_words(list_ids)


def split_str_words(list_str_words):
    list_split_words_punc = [
        long_str.translate(str.maketrans("", "", string.punctuation + "-")).split()
        for long_str in list_str_words
    ]
    return list_split_words_punc


list_split_words = split_str_words(list_str_words)


def get_rand_word():
    rand_words = []
    for list_words in list_split_words:
        rand_number = random.randint(0, len(list_words) - 1)
        word = [word for i, word in enumerate(list_words) if i == rand_number]
        rand_words.append(word[0])
    return rand_words


rand_words = get_rand_word()
