import sqlite3

class Database:
    def __init__(self, db_name="high_scores.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS scores
                               (username TEXT, score INTEGER)''')
        self.conn.commit()

    def insert_score(self, username, score):
        self.cursor.execute("INSERT INTO scores (username, score) VALUES (?, ?)", (username, score))
        self.conn.commit()

    def get_high_scores(self):
        self.cursor.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 10")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

