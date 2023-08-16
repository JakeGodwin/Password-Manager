import sqlite3


class AccountsDatabase:
    def __init__(self, db_name):
        # Create a connection to the database
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        # Create a table if it does not exist
        self.create_user_table()

    def create_user_table(self):
        # create user table with columns for user data     
        # create user table with columns for user data     
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_accounts (
                user_id INTEGER PRIMARY KEY,
                account_name TEXT NOT NULL,
                password_hash TEXT NOT NULL
            )                
        ''')
        self.conn.commit()

    def insert_account(self, user_id, account_name, password_hash):
        self.cursor.execute('''
            INSERT INTO user_accounts (user_id, account_name, password_hash)
            VALUES (?,?)
        ''', (user_id, account_name, password_hash))
        self.conn.commit()

    def get_user_accounts(self, user_id):
        # retrieve a user from the database
        self.cursor.execute('''
            SELECT account_name FROM user_accounts WHERE user_id =?
        ''', (user_id,))
        return self.cursor.fetchone()
    
    def get_user_passwords(self, user_id):
        self.cursor.execute('''
            SELECT password_hash FROM user_accounts WHERE user_id =?
        ''', (user_id,))
        password_hash = self.cursor.fetchone()
        if password_hash:
            return password_hash[0]
        else:
            return None