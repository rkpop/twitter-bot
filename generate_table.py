from CONFIG import DB_URL, TABLE_NAME
from kpopbot import Database

if __name__ == "__main__":
    Database.generate_table(DB_URL, TABLE_NAME)

