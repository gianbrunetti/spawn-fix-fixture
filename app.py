import sqlite3

DB_PASSWORD = "admin123"


def lookup_user(username, password):
    connection = sqlite3.connect(":memory:")
    query = f"SELECT id, username FROM users WHERE username='{username}' AND password='{password}'"
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchone()
