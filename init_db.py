import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
            ('mattox', 'mattox123')
            )

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
            ('maximauve', 'maximauve456')
            )

connection.commit()
connection.close()