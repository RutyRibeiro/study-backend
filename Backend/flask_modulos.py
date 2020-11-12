import inspect
import os
from werkzeug.utils import secure_filename
import tratamentoDeErros
import reco_Modulos

def verifica (request):
    body={}
    response = {}
    
    try:
        body['nome']= request.form['nome']
        body['video']= request.files['video']
    except:
        response['erro'] = 'Você esta passando a propriedade errada é apenas aceito NOME e VIDEO'
        return  response
    else:
        if body['nome'] == ''or body['nome'] is None:
            response['erro'] = 'Nome obrigatório!'
            return response
        elif body['video'] == '' or body['video'] is None:

            response['erro'] = 'Video obrigatório!'
            return response
        else:
            return body

def cadastro(body):
    response={}
    response = reco_Modulos.cadastra(body['video'], body['nome'].title())
    return response

def login(img):
    response={}
    
    if img == '' or img is None:
        
        response['erro'] = 'Você esta passando a propriedade nula ou vazia'
        
        return  response
    
    else:
        
        user = reco_Modulos.reconhece(img)
        
        if 'nome' not in user:
            response = user
        
        else:
            response['nome']=user['nome']
            response['conteudo'] = reco_Modulos.buscaConteudoUser(user['id'])

        return response

def download(file):
     try:
         filename = secure_filename(file.filename)
         file.save(os.path.join('./',secure_filename(filename)))
         return filename
     except Exception as e:
        tratamentoDeErros.printErro(os.path.basename(__file__),inspect.getframeinfo(inspect.currentframe())[2],e)
        return 'Ocorreu um erro no download'

