import sqlite3
import hashlib

class UserDatabase:
    def __init__(self, db_name):
        # Create a connection to the database
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        # Create a table if it does not exist
        self.create_user_table()

    def create_user_table(self):
        # create user table with columns for user data
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')
        self.conn.commit()
    
    def add_user(self, username, password_hash):
        # insert a new user into the database
        self.cursor.execute('''
            INSERT INTO users (username, password_hash)
            VALUES (?,?)
        ''', (username, password_hash))
        self.conn.commit()

    def get_user(self, username):
        # retrieve a user from the database
        self.cursor.execute('''
            SELECT * FROM users WHERE username =?
        ''', (username,))
        return self.cursor.fetchone()