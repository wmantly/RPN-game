import sqlite3

defaultdb = "rpngame.db"

def create_users_table():
	conn = sqlite3.connect(defaultdb)
	c = conn.cursor()
	c.execute("DROP TABLE IF EXISTS 'users'")
	c.execute(""" CREATE TABLE 'users'(
		'id' INTEGER,
		'name' VARCHAR,
		'pin' VARCHAR,
		PRIMARY KEY ('id')) 
	""")
	conn.commit()
	c.close()

def create_sessions_table():
	conn = sqlite3.connect(defaultdb)
	c = conn.cursor()
	c.execute("DROP TABLE IF EXISTS 'sessions'")
	c.execute(""" CREATE TABLE 'sessions'(
		'id' INTEGER,
		'users_id' INTEGER,
		'created_at' DATE,
		PRIMARY KEY ('id'),
		FOREIGN KEY(users_id) REFERENCES users(id)) 
	""")
	conn.commit()
	c.close()

def create_turns_table():
	conn = sqlite3.connect(defaultdb)
	c = conn.cursor()
	c.execute("DROP TABLE IF EXISTS 'turns'")
	c.execute(""" CREATE TABLE 'turns'(
		'id' INTEGER,
		'session_id' INTEGER,
		'difficulty_lvl' DATE,
		'correct_incorrect' VARCHAR,
		'time_taken' DATE,
		PRIMARY KEY ('id'),
		FOREIGN KEY (session_id) REFERENCES sessions(id)
		)""")
	conn.commit()
	c.close()
	
create_users_table()
create_turns_table()
create_sessions_table()