import sqlite3

#conexão com o banco,  se já existir ele vai se conectar. Caso contrario, ele irá criar
conn = sqlite3.connect('estudantes.db')

cursor = conn.cursor()

cursor.execute("""
    SELECT * FROM tb_estudantes
""")

print("Tabela Criada com Sucesso!")
conn.close()
