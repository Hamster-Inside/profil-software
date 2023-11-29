""" Custom Context Manager for operating on SQLite3 DB"""
import sqlite3


class SQLiteDBManager:
    """ Context Manager for SQLite"""
    def __init__(self, db_name='user_data.db'):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            if exc_type is None:
                self.conn.commit()  # Commit changes if no exception occurred
            else:
                self.conn.rollback()  # Rollback changes if an exception occurred
            self.conn.close()
