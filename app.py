import sqlite3


def lookup_user(username, identifier):
    connection = sqlite3.connect(":memory:")
    query = f"SELECT id, username FROM users WHERE username='{username}' AND id='{identifier}'"
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchone()
