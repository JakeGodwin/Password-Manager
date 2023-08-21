import sqlite3
from user_database import UserDatabase as user_db


class AccountsDatabase:
    def __init__(self, db_name):
        # Create a connection to the database
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        # Create a table if it does not exist
        self.create_user_table()

    def create_user_table(self):
        # create user table with columns for user data
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS user_accounts (
                account_id INTEGER PRIMARY KEY AUTOINCREMENT,                                  
                account_name TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES database(id)             
            )                
       ''')
        self.conn.commit()  # remove account_id set user_id to foreign key = Foreign Key REFERENCES Userdb

    def insert_account(self, account_name, password_hash, user_id):
        print("Received user_id in insert_account:", user_id)
        self.cursor.execute(
            """
            INSERT INTO user_accounts (account_name, password_hash, user_id)
            VALUES (?,?,?)
        """,
            (account_name, password_hash, user_id),
        )
        self.conn.commit()

    def get_user_accounts(self, user_id):
        # retrieve a user from the database
        self.cursor.execute(
            """
            SELECT account_name FROM user_accounts WHERE user_id =?
        """,
            (user_id,),
        )
        accounts = self.cursor.fetchall()
        account_names = [account[0] for account in accounts]
        return account_names

    def get_user_passwords(self, user_id):
        self.cursor.execute(
            """
            SELECT password_hash FROM user_accounts WHERE user_id =?
        """,
            (user_id,),
        )
        password_hash = self.cursor.fetchone()
        if password_hash:
            return password_hash[0]
        else:
            return None
