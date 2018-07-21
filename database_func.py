import sqlite3
from CONFIG import DB_URL,TABLE_NAME

def write_to_db(key):
    db=sqlite3.connect(DB_URL)
    cursor = db.cursor()
    cursor.execute('''INSERT INTO {table} VALUES(?)'''.format(table=TABLE_NAME),(key,))
    db.commit()
    db.close()

def table_check(cursor,key):
    query ='''SELECT count(*) FROM {table} WHERE ID=?'''.format(table=TABLE_NAME)
    cursor.execute(query,(key,))
    (row_count,) = cursor.fetchone()
    return True if row_count == 0 else False

def create_table(db):
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS {table}(ID TEXT)
    '''.format(table=TABLE_NAME))
    db.commit()
    
def db_checking(submissions):
    new_submissions = []
    db = sqlite3.connect(DB_URL)
    cursor = db.cursor()
    create_table(db)
    for submission in submissions:
        key = submission.id
        if table_check(cursor,key):
            new_submissions.append(submission)
    db.close()
    return new_submissions