import mysql.connector
from Database import ConfigFile

config=ConfigFile.config


def insert(lib):

    try:
        conn = mysql.connector.connect(**config)
        print("Acesso ao banco de dados: Conexão Estabelecida")
    except mysql.connector.Error as err:
        print(err)
    else:
        cursor = conn.cursor()

    nome = lib['nome']
    id = lib['id']
    insereDados = 'insert into usuarios (id_usuario,nome_usuario) values (%s,%s);'
    resul = cursor.execute(insereDados, (nome, id))

    conn.commit()
    cursor.close()
    conn.close()

    return resul


def select(id):

    try:
        conn = mysql.connector.connect(**config)
        print("Acesso ao banco de dados: Conexão Estabelecida")
    except mysql.connector.Error as err:
        print(err)
    else:
        cursor = conn.cursor()

    buscaDados = 'select nome_usuario from usuarios where id_usuario={};'.format(id)
    cursor.execute(buscaDados)
    resul = cursor.fetchall()
    nome = resul[0][0]

    conn.commit()
    cursor.close()
    conn.close()

    return nome

def buscaConteudo(id):

    try:
        conn = mysql.connector.connect(**config)
        print("Acesso ao banco de dados: Conexão Estabelecida")
    except mysql.connector.Error as err:
        print(err)
    else:
        cursor = conn.cursor()

    buscaDados = 'select * from agrotoxicos where nivel_usuario <= (select nivel_usuario from usuarios where id_usuario={}) order by nivel_usuario;'.format(id)
    cursor.execute(buscaDados)
    resul = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()

    return resul

def testaconexao():

    try:
        conn = mysql.connector.connect(**config)
        print("Acesso ao banco de dados: Conexão Estabelecida")
    except mysql.connector.Error as err:
        print(err)
    else:
        cursor = conn.cursor()

    conn.commit()
    cursor.close()
    conn.close()

testaconexao()