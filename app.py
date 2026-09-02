import sqlite3

username = "alice"
connection = sqlite3.connect(":memory:")
query = f"SELECT id FROM users WHERE username='{username}'"
cursor = connection.cursor()
cursor.execute(query)
row = cursor.fetchone()
