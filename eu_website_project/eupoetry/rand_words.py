import sqlite3
import random
import json
from pathlib import Path


path_db = Path.cwd() / "verses.sqlite3"
print("path_______", path_db)


# connect to db and get a verse from the main db
def connect_to_dbsqlite3():
    path_db = Path.cwd() / "verses.sqlite3"
    connect = sqlite3.connect(path_db)
    cur = connect.cursor()
    return connect, cur


def get_random_words():
    connect, cur = connect_to_dbsqlite3()
    all_ids = cur.execute("SELECT id_json FROM id_json_words").fetchall()
    list_of_lists_id_random_word = []
    for i_d in all_ids:
        words = cur.execute(
            "SELECT words FROM id_json_words WHERE id_json=?", i_d
        ).fetchall()
        words = json.loads(words[0][0])
        random_word = words[random.randint(0, len(words) - 1)]
        list_of_lists_id_random_word.append([i_d[0], random_word])
    connect.close()
    return list_of_lists_id_random_word


list_of_lists_id_random_word = get_random_words()
print(list_of_lists_id_random_word)
