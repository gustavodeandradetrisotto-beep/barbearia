# banco.py
# Módulo responsável por abrir a conexão com o banco de dados MySQL.
# Centralizar a conexão aqui evita repetir código nos demais módulos.

import mysql.connector
from config import DB_CONFIG


def conectar():
    """
    Cria e retorna uma nova conexão com o banco de dados MySQL,
    usando as credenciais definidas em config.py.
    """
    conexao = mysql.connector.connect(**DB_CONFIG)
    return conexao
