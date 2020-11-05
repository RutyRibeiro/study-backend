import mysql.connector, os, inspect, sys
import tratamentoDeErros
import ConfigFile

nomeDoArquivo = os.path.basename(__file__)
config=ConfigFile.config

def testa():
    try:
        conn = mysql.connector.connect(**config)
        print("Acesso ao banco de dados: Conexão Estabelecida - INSERT")
    except mysql.connector.Error as err:
        tratamentoDeErros.printErro(nomeDoArquivo,inspect.getframeinfo(inspect.currentframe())[2],err)
    else:
        cursor = conn.cursor()
        cursor.close()
    
    conn.commit()
    conn.close()
    print("Fechamento do banco de dados: Com sucesso - INSERT")
testa()
    

def insert(lib):

    try:
        conn = mysql.connector.connect(**config)
        print("Acesso ao banco de dados: Conexão Estabelecida - INSERT")
    except mysql.connector.Error as err:
        tratamentoDeErros.printErro(nomeDoArquivo,inspect.getframeinfo(inspect.currentframe())[2],err)
    else:
        cursor = conn.cursor()

    nome = lib['nome']
    id = lib['id']
    insereDados = 'insert into usuarios (id_usuario,nome_usuario) values (%s,%s);'
    resul = cursor.execute(insereDados, (id, nome))

    conn.commit()
    cursor.close()
    conn.close()
    print("Fechamento do banco de dados: Com sucesso - INSERT")

    return resul


def select(id):

    try:
        conn = mysql.connector.connect(**config)
        print("Acesso ao banco de dados: Conexão Estabelecida - SELECT")
    except mysql.connector.Error as err:
        tratamentoDeErros.printErro(nomeDoArquivo,inspect.getframeinfo(inspect.currentframe())[2],err)
    else:
        cursor = conn.cursor()

    buscaDados = 'select nome_usuario from usuarios where id_usuario={};'.format(id)
    cursor.execute(buscaDados)
    resul = cursor.fetchall()
    nome = resul[0][0]

    conn.commit()
    cursor.close()
    conn.close()
    print("Fechamento do banco de dados: Com sucesso - SELECT")

    return nome

def buscaConteudo(id):

    try:
        conn = mysql.connector.connect(**config)
        print("Acesso ao banco de dados: Conexão Estabelecida - BuscaConteudo")
    except mysql.connector.Error as err:
        tratamentoDeErros.printErro(nomeDoArquivo,inspect.getframeinfo(inspect.currentframe())[2],err)
    else:
        cursor = conn.cursor()

    buscaDados = 'select * from agrotoxicos where nivel_usuario <= (select nivel_usuario from usuarios where id_usuario={}) order by periculosidade_agrotoxico desc;'.format(id)
    cursor.execute(buscaDados)
    resul = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()
    print("Fechamento do banco de dados: Com sucesso - BuscaConteudo")

    return resul

def consultaID():
    try:
        conn = mysql.connector.connect(**config)
        print("Acesso ao banco de dados: Conexão Estabelecida - ConsultaID")
    except Exception as err:
        tratamentoDeErros.printErro(nomeDoArquivo,inspect.getframeinfo(inspect.currentframe())[2],err)

    else:
        cursor = conn.cursor()

    consulta='SELECT id_usuario FROM usuarios ORDER BY id_usuario DESC limit 1'
    cursor.execute(consulta)
    resul = cursor.fetchall()

    conn.commit()  
    cursor.close()
    conn.close() 
    print("Fechamento do banco de dados: Com sucesso - ConsultaID")
    return resul[0][0]
       
        

def deleteId(id):
    try:
        conn = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        tratamentoDeErros.printErro(nomeDoArquivo,inspect.getframeinfo(inspect.currentframe())[2],err)
    else:
        cursor = conn.cursor()

        deletaLinha=('delete from usuarios where id_usuario={}').format(id)
        cursor.execute(deletaLinha)

        cursor.close()
    
    conn.commit()
    conn.close()

    



