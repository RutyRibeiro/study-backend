from flask import request
import uteis, os
from werkzeug.utils import secure_filename

def cadastro(body):
    response={}
    if 'nome' not in body or 'video' not in body:
        response['erro'] = 'Você esta passano a propriedade errada é apenas aceito NOME e VIDEO'
        return  response
    elif body['nome'] == ''or body['nome'] is None:

        response['erro'] = 'Nome obrigatório!'
        return response
    elif body['video'] == '' or body['video'] is None:

        response['erro'] = 'Video obrigatório!'
        return response
    else:
        response = uteis.captura(body['video'], body['nome'])
        uteis.treinaAlgoritmo()
        return response
def login(img):
    response={}
    if img == '' or img is None:
        response['erro'] = 'Você esta passando a propriedade nula ou vazia'
        return  response
    else:
        response = uteis.reconheceFoto(img)
        return response
def download(file):
     try:
         filename = secure_filename(file.filename)
         file.save(os.path.join('/Users/Ruty Ribeiro/Documents/MeusProjetos/estudy-backend/Backend',
                                        secure_filename(filename)))
         return filename
     except Exception as e:
         print(e)
         return 'Ocorreu um erro no download '
