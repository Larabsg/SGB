import sqlite3

con_sqlite = sqlite3.connect('banco.db')
cur = con_sqlite.cursor()

cur.execute('''
INSERT INTO conta VALUES (2, 'lara2','12345','1234',1234,1000);
''')