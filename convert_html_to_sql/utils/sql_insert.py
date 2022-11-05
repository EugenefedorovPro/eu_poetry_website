from mysql.connector import connect


def connect_db():
    db = connect(
        host="localhost", user="root", password="sql_1980", database="eu_verses"
    )
    return db


db = connect_db()

db_cursor = db.cursor()


def get_db_name(db_cursor):
    db_cursor.execute("SELECT DATABASE()")
    db_name = db_cursor.fetchall()[0][0]
    return db_name


def insert_verse_to_db(insert_verse, val):
    db_cursor.execute(insert_verse, val)
    db.commit()
    db_cursor.execute("SELECT * FROM raw_verses")
    return db_cursor.fetchall()


def check_sql_result(db_cursor):
    db_cursor.execute("SELECT id, file_name, title FROM raw_verses")
    return db_cursor.fetchall()
