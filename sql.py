import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT
    )
''')

cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('JohnDoe', 'john@example.com'))

conn.commit()
conn.close()
