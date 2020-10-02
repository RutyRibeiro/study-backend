from flask import request
import uteis

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

