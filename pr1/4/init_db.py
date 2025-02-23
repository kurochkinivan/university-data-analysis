import sqlite3;
 
con = sqlite3.connect("sqllite.db")
cursor = con.cursor()

with open("init.sql", "r") as f:
    sql_script = f.read()

cursor.executescript(sql_script)

con.commit()
con.close()