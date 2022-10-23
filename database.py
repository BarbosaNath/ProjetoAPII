import sqlite3

def create_table(database: str,):
    con = sqlite3.connect(database)
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE {}""".format())
    
    con.commit()
    con.close() 

con = sqlite3.connect(".db")

produtos = "roupas"

cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
	id int PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	email VARCHAR(80) NOT NULL,
	login VARCHAR(80) NOT NULL,
	password VARCHAR(80) NOT NULL
);""")

cursor.execute(f"""
CREATE TABLE IF NOT EXISTS {produtos} (
	id int PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	email VARCHAR(80) NOT NULL,
	login VARCHAR(80) NOT NULL,
	password VARCHAR(80) NOT NULL
);""")

con.commit()
con.close() 