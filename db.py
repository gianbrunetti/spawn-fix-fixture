import sqlite3


def fetch_user(username, password):
    connection = sqlite3.connect(":memory:")
    query = "SELECT id, username FROM users WHERE username=? AND password=?"
    cursor = connection.cursor()
    cursor.execute(query, (username, password))
    return cursor.fetchone()
