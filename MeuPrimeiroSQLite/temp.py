import sqlite3

#conexão com o banco,  se já existir ele vai se conectar. Caso contrario, ele irá criar
conn = sqlite3.connect('estudantes.db')

cursor = conn.cursor()
lista = [('Samuel', 'Rua Manoel Severino', 1999-08-14, 201613710021), ('Samuel', 'Rua Manoel Severino', 1999-08-14, 201613710021)]
cursor.executemany("""
    INSERT INTO tb_estudantes (nome, endereco, nascimento, matricula)
    VALUES (?,?,?,?)
""", lista)
conn.commit()
print('Dados inseridos com sucesso.')
conn.close()
