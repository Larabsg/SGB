import sqlite3
import os.path
# from sqlite3 import Error

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR,"banco.db")
with sqlite3.connect(db_path) as con_sqlite:
# con_sqlite = sqlite3.connect('banco.db')
    cur = con_sqlite.cursor()

# cur.execute('''
# INSERT INTO conta (nome, cpf, nConta, senha, saldo ) VALUES ('lara2','12345','1234',1234,1000);
# ''')