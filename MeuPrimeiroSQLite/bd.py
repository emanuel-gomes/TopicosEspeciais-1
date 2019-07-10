import sqlite3

#conexão com o banco,  se já existir ele vai se conectar. Caso contrario, ele irá criar
conn = sqlite3.connect('estudantes.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE tb_estudante (
    id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(30) NOT NULL,
    endereco TEXT NOT NULL,
    nascimento DATE NOT NULL,
    matricula VARCHAR(12)
    );
""")

print("Tabela Criada com Sucesso!")
conn.close()
