"""
1 - pip install mysql-connector-python
2 - import (mysql.connector)
"""
import mysql.connector
from dados import tela_de_cadastro
from dados_clientes import CadastroClientes

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tahech02=",
    database="dados_dos_clientes",
)

cursor = conexao.cursor()

cpf, nome, sexo, data_nascimento = tela_de_cadastro()
clientes = CadastroClientes(cpf, nome, sexo, data_nascimento)
clientes.cadastro()


# CRUD
print("Inserindo dados no banco...")
comando_sql = f'''
    INSERT INTO clientes (
    cpf,
    nome,
    sexo,
    data_nascimento) VALUES (
    {clientes.banco_de_dados['cpf']}, 
    "{clientes.banco_de_dados['nome']}",
    "{clientes.banco_de_dados['sexo']}",
    "{clientes.banco_de_dados['data_nascimento']}");
'''
cursor.execute(comando_sql)
conexao.commit()
cursor.close()
conexao.close()


