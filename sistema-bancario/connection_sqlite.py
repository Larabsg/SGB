import sqlite3

con_sqlite = sqlite3.connect('banco.db')
cur = con_sqlite.cursor()

# cur.execute('''
# INSERT INTO conta (nome, cpf, senha, nConta, saldo) VALUES ('edsom','02156196338','1234',2345,1500);
# ''')