# database.py

import sqlite3

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS moderation_actions (
                            id INTEGER PRIMARY KEY,
                            action_type TEXT,
                            user_id INTEGER,
                            timestamp TEXT,
                            details TEXT
                        )''')
        self.conn.commit()

    def log_moderation_action(self, action_type, user_id, timestamp, details):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO moderation_actions (action_type, user_id, timestamp, details)
                          VALUES (?, ?, ?, ?)''', (action_type, user_id, timestamp, details))
        self.conn.commit()

    def get_moderation_logs(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM moderation_actions''')
        rows = cursor.fetchall()
        return rows

    def close_connection(self):
        self.conn.close()

# End of database.py