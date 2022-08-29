
import sqlite3
from sqlite3 import Error


# connection to the database
def createConnection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('Connection to sql db successful')
    except Error as e:
        print(f"the error {e} occurred")
        exit
    return connection

connection = createConnection('passwords.sqlite')

create_users_table = """
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

"""

create_password_table = """
CREATE TABLE IF NOT EXISTS passwords(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website TEXT NOT NULL,
    password TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

"""
def execute_query(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f'The error {e} occurred')

execute_query(connection, create_users_table)
execute_query(connection, create_password_table)
