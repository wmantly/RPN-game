import sqlite3

defaultdb = "rpngame.db"

def create_user_table():
    conn = sqlite3.connect(defaultdb)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS 'user'")
    c.execute(""" CREATE TABLE 'user'(
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
        'user_id' INTEGER,
        'created_at' TIMESTAMP DEFAULT CURRENT_TIME,
        PRIMARY KEY ('id'),
        FOREIGN KEY(user_id) REFERENCES user(id)) 
    """)
    conn.commit()
    c.close()

def create_turns_table():
	conn = sqlite3.connect(defaultdb)
	c = conn.cursor()
	c.execute("DROP TABLE IF EXISTS 'turns'")
	c.execute(""" CREATE TABLE 'turns'(
		'id' INTEGER PRIMARY KEY ,
		'session_id' INTEGER,
		'difficulty_lvl' INTEGER,
		'correct_incorrect' VARCHAR,
		'time_taken' INTEGER,
		FOREIGN KEY (session_id) REFERENCES sessions(id)
		)""")
	conn.commit()
	c.close()
	
create_user_table()
create_turns_table()
create_sessions_table()