import sqlite3
import pygame 
import objectsPool as pool # import the pool objects

conn = sqlite3.connect('users.db')
print("Opened database successfully")

cursor = conn.cursor()

# if there is no table, create one:
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
pool.ball((1,0), (255,0,0), (0,0))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
