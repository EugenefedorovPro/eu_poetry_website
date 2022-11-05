from pathlib import Path
from utils.scrape import get_file_names, scrape_verse
from utils.sql_insert import (
    db_cursor,
    get_db_name,
    insert_verse_to_db,
    check_sql_result,
)

directiry_name = "verses"
file_names = get_file_names(directiry_name)
print("number of file_names -", len(file_names))


def get_list_time_h1_main(file_names):
    list_time_h1_main = []
    for fn_as_path in file_names:
        path = Path.cwd() / directiry_name / fn_as_path
        time_h1_main = scrape_verse(path)
        list_time_h1_main.append(time_h1_main)
    return list_time_h1_main


list_time_h1_main = get_list_time_h1_main(file_names)
print("number of tuples time_h1_main -", len(list_time_h1_main))

print("name of the current db", get_db_name(db_cursor))

# file_name, data_of_writing, title, verses


def insert_verse_to_sql(file_names, list_time_h1_main):
    insert_verse = """
        INSERT INTO raw_verses (file_name, date_of_writing, title, verses) 
        VALUES (%s, %s, %s, %s);"""
    for fn, time_h1_main in zip(file_names, list_time_h1_main):
        val = (fn, time_h1_main[0], time_h1_main[1], time_h1_main[2])
        insert_verse_to_db(insert_verse, val)


insert_verse_to_sql(file_names, list_time_h1_main)

print(check_sql_result(db_cursor))
