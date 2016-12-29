import sqlite3
def createDB():
	conn = sqlite3.connect("pacromDB.db")

	c = conn.cursor()

	c.execute("""CREATE TABLE localUser (uname TEXT UNIQUE NOT NULL) """)
	

	c.execute("""CREATE TABLE chatUser (uid INTEGER PRIMARY KEY ASC AUTOINCREMENT, uName TEXT UNIQUE NOT NULL, uPw TEXT NOT NULL, displayName TEXT NOT NULL, message TEXT, status TEXT NOT NULL )""" )

createDB() 

