import sqlite3


class DatabaseConnection:

    def __init__(self, db_path: str):
        self.db_path = db_path

    def create_connection(self):
        return sqlite3.connect(self.db_path)

    def create_new_parts_database_file(self, db_file_name):
        try:
            conn = sqlite3.connect(db_file_name)
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE parts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            part_number TEXT NOT NULL,
            part_quantity INTEGER NOT NULL,
            finished BOOLEAN,
            created_at DATE,
            deadline_date DATE,
            parts_done_quantity INTEGER NOT NULL DEFAULT '0',
            email_sent_status BOOLEAN DEFAULT 'FALSE'
            )''')
            conn.commit()
            self.db_path = db_file_name
        except sqlite3.Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
