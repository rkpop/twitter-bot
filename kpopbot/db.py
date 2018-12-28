import sqlite3


class Database:
    def __init__(self, file_name, table_name):
        self.db = sqlite3.connect(file_name)
        self.table_name = table_name

    def check_table(self, key):
        cursor = self.db.cursor()
        query = """SELECT count(*) FROM {table} WHERE ID=?""".format(
            table=self.table_name
        )
        cursor.execute(query, (key,))
        (row_count,) = cursor.fetchone()
        return row_count == 0

    def write_table(self, key):
        cursor = self.db.cursor()
        query = """INSERT into {table} VALUES(?)""".format(
            table=self.table_name
        )
        cursor.execute(query, (key,))
        self.db.commit()
        return key

    @staticmethod
    def generate_table(file_name, table_name):
        db = sqlite3.connect(file_name)
        cursor = db.cursor()
        cursor.execute(
            """
        CREATE TABLE {table}(ID TEXT)
        """.format(
                table=table_name
            )
        )
        db.commit()
        db.close()
