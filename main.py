import sqlite3

conn = sqlite3.connect('users.db')
print("Opened database successfully")

cursor = conn.cursor()
cursor.execute("""
	CREATE TABLE IF NOT EXISTS users (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		firstName	TEXT NOT NULL,
		lastName	TEXT NOT NULL,
		userName	TEXT NOT NULL,
		email	TEXT NOT NULL,
		password	TEXT NOT NULL,
		highScore	INTEGER
	);
""")
print("Table created successfully")
