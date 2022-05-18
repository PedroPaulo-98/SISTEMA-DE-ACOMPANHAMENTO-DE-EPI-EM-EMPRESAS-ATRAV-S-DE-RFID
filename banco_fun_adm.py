import sqlite3


def conexao():
    return sqlite3.connect('banco_adm.sqlite')

con = conexao()
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS fun_adm
    (
        nome_funcionario  TEXT PRIMARY KEY, 
        senha_funcionario TEXT NOT NULL
    )
''')

con.commit()
con.close()