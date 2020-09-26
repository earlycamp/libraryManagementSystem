import sqlite3

conn = sqlite3.connect('all_books.db')
c = conn.cursor()


c.execute('CREATE TABLE IF NOT EXISTS comics (name TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS math (name TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS gaming (name TEXT)')

c.execute('INSERT INTO comics VALUES("Tintin")')
c.execute('INSERT INTO comics VALUES("Middle school")')
c.execute('INSERT INTO comics VALUES("Peter Pan")')
c.execute('INSERT INTO comics VALUES("Awsome james")')

c.execute('INSERT INTO math VALUES("Primary math")')
c.execute('INSERT INTO math VALUES("Spotlight math")')

c.execute('INSERT INTO gaming VALUES("Tricks of minecraft")')
c.execute('INSERT INTO gaming VALUES("100 stuff yu never new in minecraft")')



# c.execute('SELECT * FROM comics')
# c.execute('SELECT * FROM math')
# c.execute('SELECT * FROM gaming')
# print(c.fetchall())