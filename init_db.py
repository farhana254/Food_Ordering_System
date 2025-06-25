import sqlite3

with open("db_setup.sql", "r") as file:
    sql_script = file.read()

conn = sqlite3.connect("campusfood.db")
cursor = conn.cursor()
cursor.executescript(sql_script)
conn.commit()
conn.close()

print("Database created successfully with sample data.")
